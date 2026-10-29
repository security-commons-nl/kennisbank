// Toetst het sorteren op profiel (plan het profiel, stap 2b) zoals een lezer het ziet: het echte script uit
// de gebouwde pagina's, op de echte kaarten en de echte regels uit profielregels.json, met een nagebootste
// browser (localStorage, sessionStorage, de kaartengroepen).
//
// Draaien: node tools/test_profielsortering.js   (na python tools/build.py)
//
// Wat vast moet staan: zonder profiel verandert er niets; met een profiel komen de passende stukken vooraan in
// hun groep, in de volgorde van de redactie, met een etiket waarom; er verdwijnt nooit een kaart; uitgezet voor
// de sessie blijft de volgorde gewoon; een situatie of instrument verschijnt als link in de balk.
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const ontsnap = s => s.replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>').replace(/&amp;/g, '&');

let fouten = 0;
function toets(naam, ok, extra) {
  console.log((ok ? '  ok   ' : '  FOUT ') + naam + (ok || extra === undefined ? '' : '  (' + extra + ')'));
  if (!ok) fouten++;
}

function element(tag) {
  return { tag, kinderen: [], textContent: '', hidden: false, className: '', href: '', _h: {},
    appendChild(k) { this.kinderen.push(k); return k; },
    addEventListener(s, f) { this._h[s] = f; } };
}

// Een pagina inlezen: per kaartengroep de kaarten in volgorde, het script en de regels.
function laad(bestand) {
  const html = fs.readFileSync(path.join(ROOT, bestand), 'utf8');
  const delen = html.split(/<div class="grid"/).slice(1);
  // Elk deel loopt tot de volgende groep; binnen een kaart staan zelf ook </div>'s, dus niet daarop knippen.
  const grids = delen.map(deel => {
    const kaarten = [...deel.matchAll(/<a class="item" href="([^"]*)" data-vak="([^"]*)" data-zoek="[^"]*" data-barrieres="([^"]*)" data-normen="([^"]*)"/g)]
      .map(m => Object.assign(element('a'), { href: m[1], attrs: { 'data-vak': m[2], 'data-barrieres': ontsnap(m[3]), 'data-normen': ontsnap(m[4]) },
        getAttribute(n) { return n in this.attrs ? this.attrs[n] : null; } }));
    const grid = { kaarten,
      querySelectorAll: () => grid.kaarten.slice(),
      appendChild(k) { grid.kaarten = grid.kaarten.filter(x => x !== k); grid.kaarten.push(k); return k; } };
    return grid;
  }).filter(g => g.kaarten.length);
  const regels = ontsnap((html.match(/<script type="application\/json" id="profielregels">([\s\S]*?)<\/script>/) || [])[1] || '');
  const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).find(s => s.includes("'commons-profiel'"));
  return { grids, regels, script };
}

function draai(bestand, profiel, sessie) {
  const pagina = laad(bestand);
  const voor = pagina.grids.map(g => g.kaarten.map(k => k.href));
  const balk = Object.assign(element('div'), { hidden: true });
  const opslag = { 'commons-profiel': profiel === null ? null : JSON.stringify(profiel) };
  const sessieOpslag = Object.assign({}, sessie || {});
  const document = {
    getElementById: id => (id === 'profielbalk' ? balk : id === 'profielregels' ? { textContent: pagina.regels } : null),
    querySelectorAll: sel => (sel === '.grid' ? pagina.grids : []),
    createElement: tag => element(tag),
  };
  const localStorage = { getItem: k => (k in opslag ? opslag[k] : null) };
  const sessionStorage = { getItem: k => (k in sessieOpslag ? sessieOpslag[k] : null), setItem: (k, v) => { sessieOpslag[k] = v; } };
  new Function('document', 'localStorage', 'sessionStorage', 'location', pagina.script)(document, localStorage, sessionStorage, { reload() {} });
  const tekst = el => [el.textContent, ...el.kinderen.map(tekst)].join('');
  return { pagina, voor, na: pagina.grids.map(g => g.kaarten.map(k => k.href)), balk, tekst: tekst(balk),
    links: balk.kinderen.flatMap(p => p.kinderen.filter(k => k.tag === 'a').map(a => a.href)) };
}

// Vooraan staan de passende kaarten in hun oude volgorde, daarna de rest in de oude volgorde.
function klopt(voor, na, passend) {
  const verwacht = voor.filter(h => passend.has(h)).concat(voor.filter(h => !passend.has(h)));
  return JSON.stringify(verwacht) === JSON.stringify(na);
}

const SEC = 'security/index.html';

let r = draai(SEC, null);
toets('het script en de regels staan op de pagina', !!r.pagina.script && r.pagina.regels.includes('cbw-plicht'));
toets('zonder profiel: niets verplaatst, balk verborgen', JSON.stringify(r.voor) === JSON.stringify(r.na) && r.balk.hidden);

r = draai(SEC, { cbw: 'essentieel' });
const cbw = new Set(r.pagina.grids.flatMap(g => g.kaarten).filter(k => /(^|\|)(Cbw|NIS2)(\||$)/.test(k.getAttribute('data-normen'))).map(k => k.href));
toets('Cbw essentieel: er zijn stukken met Cbw of NIS2 op security', cbw.size > 0, cbw.size);
toets('Cbw essentieel: die staan vooraan in hun groep, in de volgorde van de redactie',
  r.voor.every((v, i) => klopt(v, r.na[i], cbw)));
toets('Cbw essentieel: de volgorde is echt veranderd (anders bewijst "vooraan" niets)',
  JSON.stringify(r.voor) !== JSON.stringify(r.na));
toets('er verdwijnt geen kaart', r.voor.flat().length === r.na.flat().length && r.voor.flat().every(h => r.na.flat().includes(h)));
const etiket = r.pagina.grids.flatMap(g => g.kaarten).filter(k => cbw.has(k.href))
  .every(k => k.kinderen.some(e => e.className === 'profieletiket' && e.textContent.includes('Cyberbeveiligingswet')));
toets('elk vooraan gezet stuk heeft een etiket met het waarom', etiket);
toets('de balk is zichtbaar en noemt het aantal',
  !r.balk.hidden && r.tekst.includes(cbw.size + (cbw.size === 1 ? ' stuk eerst' : ' stukken eerst')), r.tekst);
toets('er staan meer kaarten in een groep dan alleen de passende', r.pagina.grids.some(g => g.kaarten.length > 5));
toets('de balk wijst naar /profiel/', r.links.includes('/profiel/'));

r = draai(SEC, { cbw: 'essentieel' }, { 'commons-profiel-sortering': 'uit' });
toets('sortering uit voor de sessie: niets verplaatst', JSON.stringify(r.voor) === JSON.stringify(r.na));
toets('sortering uit: de balk zegt het, met een knop om weer te sorteren', !r.balk.hidden && r.tekst.includes('staat uit'), r.tekst);

r = draai(SEC, { capaciteit: 'geen' });
toets('geen eigen ISO: de balk wijst naar de route van de eerste honderd dagen',
  r.links.includes('https://security-commons-nl.github.io/#route-eerste-honderd-dagen'), r.links.join(' '));
toets('geen eigen ISO raakt geen stukken: de volgorde blijft', JSON.stringify(r.voor) === JSON.stringify(r.na));

r = draai(SEC, { ot: 'substantieel' });
toets('OT substantieel: de balk wijst naar de CSIR-tool', r.links.includes('https://security-commons-nl.github.io/csir-assessment-tool/'));

r = draai(SEC, { cbw: 'bestaat-niet', detectie: ['onzin'] });
toets('een onbekend antwoord doet niets', JSON.stringify(r.voor) === JSON.stringify(r.na) && r.balk.hidden);

r = draai(SEC, { detectie: 'geen' });
const soc = new Set(r.pagina.grids.flatMap(g => g.kaarten).filter(k => /\b(soc|edr)\b/.test(k.getAttribute('data-barrieres'))).map(k => k.href));
toets('geen detectie: de stukken met barriere soc of edr staan vooraan', soc.size > 0 && r.voor.every((v, i) => klopt(v, r.na[i], soc)), soc.size);

r = draai('privacy/index.html', { gevoelig: ['jeugd'] });
toets('jeugd als gevoelig domein: op privacy staan alle stukken vooraan (en blijven in volgorde)',
  JSON.stringify(r.voor) === JSON.stringify(r.na) && !r.balk.hidden);

r = draai('index.html', { politiegegevens: 'ja' });
const wpg = new Set(r.pagina.grids.flatMap(g => g.kaarten).filter(k => /(^|\|)Wpg(\||$)/.test(k.getAttribute('data-normen'))).map(k => k.href));
toets('root: politiegegevens zet de Wpg-stukken vooraan', wpg.size > 0 && r.voor.every((v, i) => klopt(v, r.na[i], wpg)), wpg.size);

console.log(fouten ? `\n${fouten} fout(en).` : '\nAlles goed.');
process.exit(fouten ? 1 : 0);
