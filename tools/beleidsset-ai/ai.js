/* De AI-hulp van de beleidsset: zeven stappen, van sleutel tot voorstel.
 *
 * Overgenomen uit procescheck (ai/bron/ai.js); het patroon staat in het plan AI-hulp met eigen sleutel.
 * Dit is het enige bestand dat naar buiten praat. De sleutel staat in sessionStorage en nergens anders;
 * het voorstel bevat de sha256 van de invoer, niet de invoer zelf en niet de sleutel. Het model krijgt de
 * systeemprompt van de opdracht, de lijst met vragen of invulvelden en een stuk invoer; nooit het beleid zelf.
 */
(function () {
  'use strict';

  var OPDRACHTEN = window.__OPDRACHTEN__;
  var kern = window.kern;
  var SLEUTEL_OPSLAG = 'beleidsset-ai-sleutel';
  var LEVERANCIER_OPSLAG = 'beleidsset-ai-leverancier';

  function el(id) { return document.getElementById(id); }
  function maak(tag, tekst, attributen) {
    var knoop = document.createElement(tag);
    if (tekst !== null && tekst !== undefined) knoop.textContent = String(tekst);
    if (attributen) Object.keys(attributen).forEach(function (n) { knoop.setAttribute(n, String(attributen[n])); });
    return knoop;
  }
  function leegMaken(knoop) { while (knoop.firstChild) knoop.removeChild(knoop.firstChild); return knoop; }
  function vandaag() {
    var nu = new Date();
    return nu.getFullYear() + '-' + String(nu.getMonth() + 1).padStart(2, '0') + '-' + String(nu.getDate()).padStart(2, '0');
  }
  function sha256(tekst) {
    return crypto.subtle.digest('SHA-256', new TextEncoder().encode(tekst)).then(function (buf) {
      return Array.prototype.map.call(new Uint8Array(buf), function (b) { return b.toString(16).padStart(2, '0'); }).join('');
    });
  }

  var stand = {
    leverancier: null, basis: '', model: '', sleutel: '', verbonden: false,
    opdracht: null, invoerNaam: '', invoerTekst: '', toestemming: false,
    bezig: false, stoppen: false, voorstel: null
  };

  // ── De parameter van een opdracht: de vragen of de invulvelden ─────────────

  function vraagVan(id) {
    return OPDRACHTEN.vragen.filter(function (v) { return v.id === id; })[0] || null;
  }

  function parameterTekst(opdracht) {
    if (opdracht.parameter === 'vragen') {
      return 'Contextvragen:\n' + OPDRACHTEN.vragen.map(function (v) {
        return '- ' + v.id + ': ' + v.vraag + (v.meerdere ? ' (meerdere antwoorden mogelijk)' : ' (een antwoord)') +
          '\n  antwoorden: ' + v.antwoorden.map(function (a) { return a.id + ' = ' + a.label; }).join('; ');
      }).join('\n');
    }
    return 'Invulvelden:\n' + OPDRACHTEN.velden.map(function (v) {
      return '- ' + v.naam + (v.toelichting ? ': ' + v.toelichting : '');
    }).join('\n');
  }

  /* Wat het model teruggeeft, gelegd tegen de vaste lijsten. Een vraag of veld dat niet bestaat, een
     antwoord dat niet in de lijst staat en een tweede item voor dezelfde code gaan eruit, met een melding.
     Elk item krijgt citaat_klopt uit de citaatcontrole van de kern. */
  function legTegenLijsten(opdracht, samen, invoer) {
    var items = [], gezien = {}, waarschuwingen = [], onzeker = samen.onzeker.slice();
    (samen.items || []).forEach(function (item) {
      var code = String(item.code || '').replace(/-\d+$/, function (staart) {
        return (opdracht.parameter === 'vragen' ? vraagVan(item.code) : OPDRACHTEN.velden.some(function (v) { return v.naam === item.code; }))
          ? staart : '';
      });
      if (gezien[code]) {
        onzeker.push('Voor "' + code + '" gaf de tekst meer dan een kandidaat; de eerste staat in het voorstel, de andere was: ' +
          (item.waarde || (item.antwoorden || []).join(', ')) + '.');
        return;
      }
      var uit = { code: code, bronregel: item.bronregel };
      if (opdracht.parameter === 'vragen') {
        var vraag = vraagVan(code);
        if (!vraag) { waarschuwingen.push('Onbekende vraag "' + code + '" weggelaten.'); return; }
        var geldig = vraag.antwoorden.map(function (a) { return a.id; });
        var antwoorden = (item.antwoorden || []).filter(function (a) { return geldig.indexOf(a) >= 0; });
        if (antwoorden.length < (item.antwoorden || []).length) {
          waarschuwingen.push('Bij "' + code + '" stond een antwoord dat niet in de lijst staat; weggelaten.');
        }
        if (!antwoorden.length) return;
        if (!vraag.meerdere && antwoorden.length > 1) {
          onzeker.push('Bij "' + vraag.vraag + '" noemde de tekst meer dan een antwoord; alleen het eerste staat in het voorstel.');
          antwoorden = antwoorden.slice(0, 1);
        }
        uit.antwoorden = antwoorden;
      } else {
        if (!OPDRACHTEN.velden.some(function (v) { return v.naam === code; })) {
          waarschuwingen.push('Onbekend invulveld "' + code + '" weggelaten.');
          return;
        }
        if (!String(item.waarde || '').trim()) return;
        uit.waarde = String(item.waarde).trim();
      }
      uit.citaat_klopt = kern.bronregel_klopt(uit, invoer);
      gezien[code] = true;
      items.push(uit);
    });
    return { items: items, onzeker: onzeker, waarschuwingen: waarschuwingen };
  }

  // ── Sleutel ───────────────────────────────────────────────────────────────

  function leesSleutel() {
    try { return window.sessionStorage.getItem(SLEUTEL_OPSLAG) || ''; } catch (f) { return ''; }
  }
  function bewaarSleutel(sleutel) {
    try {
      if (sleutel) window.sessionStorage.setItem(SLEUTEL_OPSLAG, sleutel);
      else window.sessionStorage.removeItem(SLEUTEL_OPSLAG);
    } catch (f) { /* privémodus: dan alleen in het geheugen */ }
  }

  // ── Stappen aan en uit ────────────────────────────────────────────────────

  function zetStap(id, actief) {
    el(id).setAttribute('data-actief', actief ? 'ja' : 'nee');
  }

  function werkStappenBij() {
    zetStap('stap-opdracht', stand.verbonden);
    zetStap('stap-invoer', stand.verbonden && !!stand.opdracht);
    var heeftInvoer = stand.invoerTekst.trim().length > 0;
    zetStap('stap-toestemming', stand.verbonden && !!stand.opdracht && heeftInvoer);
    zetStap('stap-uitvoeren', stand.verbonden && !!stand.opdracht && heeftInvoer && stand.toestemming);
    el('knop-uitvoeren').disabled = !(stand.verbonden && stand.opdracht && heeftInvoer && stand.toestemming) || stand.bezig;
    zetStap('stap-voorstel', !!stand.voorstel);
    zetStap('stap-verder', !!stand.voorstel);
    el('knop-verbinding').disabled = !stand.sleutel || !stand.basis;
    tekenToestemming();
  }

  // ── Stap 1: leverancier ───────────────────────────────────────────────────

  function kiesLeverancier(id, behoudVelden) {
    var lev = OPDRACHTEN.leveranciers.filter(function (l) { return l.id === id; })[0] || OPDRACHTEN.leveranciers[0];
    stand.leverancier = lev.id;
    if (!behoudVelden) {
      stand.basis = lev.basis;
      stand.model = lev.model;
      el('lev-basis').value = lev.basis;
      el('lev-model').value = lev.model;
    }
    el('lev-uitleg').textContent = lev.uitleg;
    try { window.localStorage.setItem(LEVERANCIER_OPSLAG, lev.id); } catch (f) { /* niets */ }
    stand.verbonden = false;
    el('lev-status').textContent = '';
    werkStappenBij();
  }

  function tekenLeveranciers() {
    var doel = leegMaken(el('lev-keuzes'));
    OPDRACHTEN.leveranciers.forEach(function (lev) {
      var label = maak('label', null, { 'class': 'vink' });
      var radio = maak('input', null, { type: 'radio', name: 'leverancier', value: lev.id, 'data-leverancier': lev.id });
      radio.addEventListener('change', function () { kiesLeverancier(lev.id, false); });
      label.appendChild(radio);
      label.appendChild(document.createTextNode(' ' + lev.naam));
      doel.appendChild(label);
    });
  }

  function testVerbinding() {
    var status = el('lev-status');
    status.textContent = 'verbinden...';
    status.className = '';
    stand.verbonden = false;
    return fetch(stand.basis.replace(/\/+$/, '') + '/v1/models', {
      method: 'GET', headers: { Authorization: 'Bearer ' + stand.sleutel }
    }).then(function (antwoord) {
      if (antwoord.status === 401 || antwoord.status === 403) throw new Error('sleutel geweigerd (HTTP ' + antwoord.status + ')');
      if (!antwoord.ok) throw new Error('HTTP ' + antwoord.status);
      stand.verbonden = true;
      status.textContent = 'verbonden';
      status.className = 'status-ok';
    }).catch(function (fout) {
      status.textContent = 'niet verbonden: ' + fout.message +
        (fout.message === 'Failed to fetch' ? ' (geen verbinding; bij Ollama: staat OLLAMA_ORIGINS goed?)' : '');
      status.className = 'status-fout';
    }).then(werkStappenBij);
  }

  // ── Stap 2 en 3: opdracht en invoer ───────────────────────────────────────

  function tekenOpdrachten() {
    var keuze = el('opdracht-keuze');
    keuze.appendChild(maak('option', 'kies een opdracht', { value: '' }));
    OPDRACHTEN.opdrachten.forEach(function (o) { keuze.appendChild(maak('option', o.titel, { value: o.id })); });
  }

  function opdrachtVan(id) {
    return OPDRACHTEN.opdrachten.filter(function (o) { return o.id === id; })[0] || null;
  }

  function kiesOpdracht(id) {
    stand.opdracht = opdrachtVan(id);
    el('opdracht-uitleg').textContent = stand.opdracht ? stand.opdracht.uitleg : '';
    el('invoer-soorten').textContent = stand.opdracht ? stand.opdracht.invoer.filter(function (s) { return s !== 'tekst'; })
      .map(function (s) { return '.' + s; }).join(', ') : '';
    el('invoer-bestand').setAttribute('accept', stand.opdracht ? stand.opdracht.invoer
      .filter(function (s) { return s !== 'tekst'; }).map(function (s) { return '.' + s; }).join(',') : '');
    werkStappenBij();
  }

  function zetInvoer(naam, tekst) {
    stand.invoerNaam = naam;
    stand.invoerTekst = tekst;
    el('invoer-tekst').value = tekst;
    var stukken = kern.chunk(tekst, OPDRACHTEN.grenzen.max_tekens_per_aanroep);
    el('invoer-info').textContent = tekst.trim() ? (naam ? naam + ': ' : '') + tekst.length + ' tekens, ' +
      stukken.length + ' aanroep' + (stukken.length === 1 ? '' : 'en') : '';
    stand.toestemming = false;
    el('toestemming').checked = false;
    werkStappenBij();
  }

  function leesBestand(bestand) {
    var naam = bestand.name;
    if (/\.xlsx$/i.test(naam)) {
      return bestand.arrayBuffer().then(kern.xlsx_naar_tekst).then(function (tekst) { zetInvoer(naam, tekst); });
    }
    return bestand.text().then(function (tekst) {
      zetInvoer(naam, /\.csv$/i.test(naam) ? kern.csv_naar_tekst(tekst) : tekst);
    });
  }

  // ── Stap 4: toestemming ───────────────────────────────────────────────────

  function tekenToestemming() {
    var doel = leegMaken(el('toestemming-tekst'));
    if (!stand.opdracht || !stand.invoerTekst.trim()) return;
    var stukken = kern.chunk(stand.invoerTekst, OPDRACHTEN.grenzen.max_tekens_per_aanroep);
    doel.appendChild(maak('p', 'Wat er verstuurd wordt: ' + (stand.invoerNaam ? 'het bestand ' + stand.invoerNaam :
      'de geplakte tekst') + ' (' + stand.invoerTekst.length + ' tekens, in ' + stukken.length + ' aanroep' +
      (stukken.length === 1 ? '' : 'en') + '), met de opdracht "' + stand.opdracht.titel + '" en de lijst met ' +
      (stand.opdracht.parameter === 'vragen' ? 'contextvragen' : 'invulvelden') + ' uit de beleidsset.'));
    doel.appendChild(maak('p', 'Waarheen: ' + stand.basis + ' (model ' + stand.model + '), onder de voorwaarden van die leverancier.'));
    doel.appendChild(maak('p', 'Wat er niet gaat: je antwoorden in de generator, je sleutel in een bestand, en de tekst van het beleid.'));
  }

  // ── Stap 5: uitvoeren ─────────────────────────────────────────────────────

  function wacht(ms) { return new Promise(function (klaar) { setTimeout(klaar, ms); }); }

  function roepAan(berichten, vorm) {
    var body = { model: stand.model, messages: berichten, temperature: 0, response_format: vorm };
    return fetch(stand.basis.replace(/\/+$/, '') + '/v1/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + stand.sleutel },
      body: JSON.stringify(body)
    });
  }

  /* Eerst json_schema; bij een 400 daarover terugvallen op json_object. Bij 429 wachten en opnieuw. */
  function vraagModel(berichten, schema, meld) {
    var vormen = [
      { type: 'json_schema', json_schema: { name: 'voorstel', schema: schema, strict: true } },
      { type: 'json_object' }
    ];
    var wachttijden = OPDRACHTEN.grenzen.wachttijden_bij_429_seconden;
    function probeer(vormIndex, poging) {
      if (stand.stoppen) return Promise.reject(new Error('gestopt'));
      return roepAan(berichten, vormen[vormIndex]).then(function (antwoord) {
        if (antwoord.status === 400 && vormIndex === 0) {
          meld('json_schema niet geaccepteerd, opnieuw met json_object');
          return probeer(1, 0);
        }
        if (antwoord.status === 429 && poging < wachttijden.length) {
          meld('te veel verzoeken, wachten ' + wachttijden[poging] + ' s');
          return wacht(wachttijden[poging] * 1000).then(function () { return probeer(vormIndex, poging + 1); });
        }
        if (antwoord.status === 401 || antwoord.status === 403) throw new Error('sleutel geweigerd (HTTP ' + antwoord.status + ')');
        if (!antwoord.ok) throw new Error('HTTP ' + antwoord.status);
        return antwoord.json().then(function (data) {
          return data.choices[0].message.content;
        });
      });
    }
    return probeer(0, 0);
  }

  function voerUit() {
    if (stand.bezig) return;
    stand.bezig = true;
    stand.stoppen = false;
    stand.voorstel = null;
    el('knop-stoppen').disabled = false;
    werkStappenBij();
    var voortgang = el('voortgang');
    var opdracht = stand.opdracht;
    var stukken = kern.chunk(stand.invoerTekst, OPDRACHTEN.grenzen.max_tekens_per_aanroep)
      .slice(0, OPDRACHTEN.grenzen.max_aanroepen_per_opdracht);
    var systeem = opdracht.systeemprompt + '\n\n' + parameterTekst(opdracht) + '\n\n' + OPDRACHTEN.vaste_regels;
    var delen = [], waarschuwingen = [];
    var teller = 0;

    function meld(tekst) { voortgang.textContent = 'aanroep ' + (teller + 1) + ' van ' + stukken.length + ': ' + tekst; }

    function volgende() {
      if (teller >= stukken.length) return Promise.resolve();
      meld('bezig');
      var berichten = [{ role: 'system', content: systeem }, { role: 'user', content: stukken[teller] }];
      return vraagModel(berichten, opdracht.schema, meld).then(function (ruw) {
        var uitkomst = kern.parse_antwoord(opdracht.schema, ruw);
        if (uitkomst.fouten.length) {
          meld('antwoord voldeed niet aan het schema, een keer opnieuw');
          berichten.push({ role: 'assistant', content: ruw });
          berichten.push({ role: 'user', content: 'Je antwoord voldeed niet aan het schema: ' +
            uitkomst.fouten.slice(0, 5).join('; ') + '. Antwoord opnieuw, alleen JSON.' });
          return vraagModel(berichten, opdracht.schema, meld).then(function (ruw2) {
            var tweede = kern.parse_antwoord(opdracht.schema, ruw2);
            if (tweede.fouten.length) {
              waarschuwingen.push('Aanroep ' + (teller + 1) + ' gaf twee keer een ongeldig antwoord en is overgeslagen: ' + tweede.fouten[0]);
            } else {
              waarschuwingen.push('Aanroep ' + (teller + 1) + ' gaf eerst ongeldige JSON en is een keer opnieuw gedaan.');
              delen.push(tweede.data);
            }
          });
        }
        delen.push(uitkomst.data);
      }).then(function () { teller += 1; return volgende(); });
    }

    volgende().then(function () {
      return sha256(stand.invoerTekst);
    }).then(function (hash) {
      var samen = kern.voeg_stukken_samen(opdracht, delen);
      var gelegd = legTegenLijsten(opdracht, samen, stand.invoerTekst);
      stand.voorstel = {
        formaat: OPDRACHTEN.voorstel_formaat, versie: 1, tool: OPDRACHTEN.tool,
        opdrachten_versie: OPDRACHTEN.versie, set_vingerafdruk: OPDRACHTEN.set_vingerafdruk,
        opdracht: opdracht.id, gemaakt: vandaag(), leverancier: stand.leverancier, model: stand.model,
        invoer: { naam: stand.invoerNaam || 'geplakte tekst', sha256: hash, tekens: stand.invoerTekst.length, aanroepen: stukken.length },
        items: gelegd.items, onzeker: gelegd.onzeker,
        waarschuwingen: waarschuwingen.concat(gelegd.waarschuwingen)
      };
      voortgang.textContent = 'klaar: ' + stukken.length + ' aanroep' + (stukken.length === 1 ? '' : 'en') + '.';
      tekenVoorstel();
    }).catch(function (fout) {
      voortgang.textContent = fout.message === 'gestopt' ? 'gestopt' : 'mislukt: ' + fout.message +
        (fout.message === 'Failed to fetch' ? ' (geen verbinding; staat de endpoint in de CSP van deze pagina, en bij Ollama OLLAMA_ORIGINS?)' : '');
    }).then(function () {
      stand.bezig = false;
      el('knop-stoppen').disabled = true;
      werkStappenBij();
    });
  }

  // ── Stap 6: voorstel ──────────────────────────────────────────────────────

  function omschrijving(item) {
    if (item.waarde !== undefined) return item.waarde;
    var vraag = vraagVan(item.code);
    return item.antwoorden.map(function (a) {
      var gevonden = vraag.antwoorden.filter(function (x) { return x.id === a; })[0];
      return gevonden ? gevonden.label : a;
    }).join(', ');
  }

  function tekenVoorstel() {
    var v = stand.voorstel;
    var tabel = leegMaken(el('tabel-voorstel'));
    var vragen = v.opdracht === 'profiel';
    var thead = maak('thead'), kop = maak('tr');
    [vragen ? 'vraag' : 'invulveld', vragen ? 'antwoord' : 'waarde', 'citaat uit de bron'].forEach(function (k) {
      kop.appendChild(maak('th', k, { scope: 'col' }));
    });
    thead.appendChild(kop);
    tabel.appendChild(thead);
    var tbody = maak('tbody');
    var nietInBron = 0;
    v.items.forEach(function (item) {
      if (!item.citaat_klopt) nietInBron += 1;
      var tr = maak('tr', null, { 'data-item': item.code, 'class': item.citaat_klopt ? '' : 'niet-in-bron' });
      tr.appendChild(maak('td', vragen ? vraagVan(item.code).vraag : item.code));
      tr.appendChild(maak('td', omschrijving(item)));
      tr.appendChild(maak('td', (item.citaat_klopt ? '' : 'niet in de bron: ') + item.bronregel, { 'class': 'tekst' }));
      tbody.appendChild(tr);
    });
    tabel.appendChild(tbody);
    el('voorstel-samenvatting').textContent = v.items.length + (vragen ? ' beantwoorde vragen' : ' ingevulde velden') +
      (nietInBron ? ', waarvan ' + nietInBron + ' met een citaat dat niet in de bron staat (die staan in de generator standaard uit)' : '') + '.';
    var onzeker = leegMaken(el('onzeker'));
    (v.onzeker.length ? v.onzeker : ['niets gemeld']).forEach(function (t) { onzeker.appendChild(maak('li', t)); });
    var waarschuwingen = leegMaken(el('waarschuwingen'));
    v.waarschuwingen.forEach(function (t) { waarschuwingen.appendChild(maak('p', t, { 'class': 'waarschuwing' })); });
  }

  function slaVoorstelOp() {
    var v = stand.voorstel;
    var blob = new Blob([JSON.stringify(v, null, 1)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var link = document.createElement('a');
    link.href = url;
    link.download = 'beleidsset-voorstel-' + v.opdracht + '-' + v.gemaakt + '.json';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    setTimeout(function () { URL.revokeObjectURL(url); }, 0);
  }

  // ── Opstarten ─────────────────────────────────────────────────────────────

  function start() {
    el('versie').textContent = 'opdrachten ' + OPDRACHTEN.versie + ' · set ' + String(OPDRACHTEN.set_vingerafdruk).slice(0, 12);
    tekenLeveranciers();
    tekenOpdrachten();

    var onthouden = null;
    try { onthouden = window.localStorage.getItem(LEVERANCIER_OPSLAG); } catch (f) { onthouden = null; }
    var eerste = onthouden || OPDRACHTEN.leveranciers[0].id;
    document.querySelector('[data-leverancier="' + eerste + '"]').checked = true;
    kiesLeverancier(eerste, false);
    stand.sleutel = leesSleutel();
    el('lev-sleutel').value = stand.sleutel;

    el('lev-basis').addEventListener('input', function () { stand.basis = el('lev-basis').value.trim(); stand.verbonden = false; werkStappenBij(); });
    el('lev-model').addEventListener('input', function () { stand.model = el('lev-model').value.trim(); });
    el('lev-sleutel').addEventListener('input', function () {
      stand.sleutel = el('lev-sleutel').value.trim();
      bewaarSleutel(stand.sleutel);
      stand.verbonden = false;
      werkStappenBij();
    });
    el('knop-verbinding').addEventListener('click', testVerbinding);
    el('knop-sleutel-vergeten').addEventListener('click', function () {
      stand.sleutel = '';
      el('lev-sleutel').value = '';
      bewaarSleutel('');
      stand.verbonden = false;
      el('lev-status').textContent = 'sleutel vergeten';
      el('lev-status').className = '';
      werkStappenBij();
    });

    el('opdracht-keuze').addEventListener('change', function () { kiesOpdracht(el('opdracht-keuze').value); });
    el('invoer-tekst').addEventListener('input', function () { zetInvoer('', el('invoer-tekst').value); });
    el('knop-invoer-bestand').addEventListener('click', function () { el('invoer-bestand').click(); });
    el('invoer-bestand').addEventListener('change', function (g) {
      var bestand = g.target.files[0];
      if (bestand) leesBestand(bestand).catch(function (fout) { el('invoer-info').textContent = 'niet te lezen: ' + fout.message; });
      g.target.value = '';
    });
    el('toestemming').addEventListener('change', function () { stand.toestemming = el('toestemming').checked; werkStappenBij(); });
    el('knop-uitvoeren').addEventListener('click', voerUit);
    el('knop-stoppen').addEventListener('click', function () { stand.stoppen = true; });
    el('knop-voorstel-opslaan').addEventListener('click', slaVoorstelOp);

    werkStappenBij();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
