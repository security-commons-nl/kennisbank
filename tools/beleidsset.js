// Generator van de beleidsset: dezelfde rekenregel als genereer_stuk in tools/bouw_beleidsset.py.
// Wijzig ze samen; tools/test_beleidsset.py vergelijkt de uitvoer van beide op een reeks profielen.
// Werkt in de browser (window.Beleidsset) en in node (module.exports).
(function (wereld) {
  "use strict";
  var TAG = /\[(\d\.\d{2}\.\d{2}(?:,\s*\d\.\d{2}\.\d{2})*)\]/g;
  var NUMMER = /(?<![\d.])(\d\.\d{2}\.\d{2})(?![\d.])/g;
  var VELD = /\[\[([^\]:]+?)(?::\s*([^\]]+?))?\]\]/g;
  var CONTROLE = /^\|\s*([A-Z]{2,5}-\d{2,3})\s*\|/;
  var HOOFDSTUK = /^## (\d+)\. (.+)$/;
  var VOOR = 2, ACHTER = 3;  // vaste hoofdstukken voor en na de onderwerpen
  var RIJ = /^(?:> )?\|\s*([A-Z]{2,5}-\d{2,3})\s*\|/;
  var WEBPLEK = "https://security-commons-nl.github.io/kennisbank/governance/";


  function nummerRegels(regels) {
    var uit = [], teller = 0;
    regels.forEach(function (r) {
      var kader = r.indexOf("> ") === 0;
      var kern = kader ? r.slice(2) : r;
      var voor = kader ? "> " : "";
      if (kern.charAt(0) === "#") { teller = 0; uit.push(r); }
      else if (kern.indexOf("- ") === 0) { teller += 1; uit.push(voor + teller + ". " + kern.slice(2)); }
      else if (kern.indexOf("  ") === 0 && teller) uit.push(voor + " " + kern);
      else uit.push(r);
    });
    return uit;
  }

  function antwoordenVan(profiel, vraag) {
    var w = profiel[vraag];
    if (w === undefined || w === null || w === "" || (Array.isArray(w) && w.length === 0)) return null;
    return Array.isArray(w) ? w.slice() : [w];
  }

  function beoordeel(als, profiel) {
    var uitkomst = "ja";
    for (var i = 0; i < als.length; i++) {
      var v = als[i];
      var gegeven = antwoordenVan(profiel, v.vraag);
      if (gegeven === null) { uitkomst = "open"; continue; }
      var raak = gegeven.some(function (a) { return v.antwoorden.indexOf(a) >= 0; });
      if (raak === v.niet) return "nee";
    }
    return uitkomst;
  }

  function label(vragen, vraag, antwoord) {
    var lijst = vragen[vraag].antwoorden;
    for (var i = 0; i < lijst.length; i++) if (lijst[i].id === antwoord) return lijst[i].label;
    return antwoord;
  }

  function kopVanBlok(als, vragen) {
    var delen = als.map(function (v) {
      var labels = v.antwoorden.map(function (a) { return "«" + label(vragen, v.vraag, a) + "»"; }).join(" of ");
      return vragen[v.vraag].vraag + " " + (v.niet ? "niet " : "") + labels;
    });
    return "> **Alleen als: " + delen.join("; ") + "**";
  }

  function vulVelden(regel, velden) {
    return regel.replace(VELD, function (_, naam, uitleg) {
      naam = naam.trim();
      if (!velden.some(function (v) { return v[0] === naam; })) velden.push([naam, (uitleg || "").trim()]);
      return "**[" + naam + "]**";
    });
  }

  function stripNl(s) { return s.replace(/^\n+/, "").replace(/\n+$/, ""); }

  function genereerStuk(steen, data, profiel) {
    var vragen = {};
    data.profiel.vragen.forEach(function (v) { vragen[v.id] = v; });
    var domein = data.profiel.domeinen.filter(function (d) { return d.id === steen.domein; })[0];
    var regels = [], velden = [], gedekt = {}, controles = {};
    var kop = steen.titel;
    steen.delen.forEach(function (deel) {
      var oordeel = deel.als === null ? "ja" : beoordeel(deel.als, profiel);
      if (oordeel === "nee") return;
      var inhoud = deel.regels.map(function (r) { return vulVelden(r, velden); });
      deel.regels.forEach(function (r) {
        if (r.charAt(0) === "#") kop = r.replace(/^#+/, "").trim();
        r.replace(TAG, function (_, nrs) {
          nrs.split(/,\s*/).forEach(function (nr) {
            if (!(nr in gedekt)) gedekt[nr] = kop;
          });
          return _;
        });
        var c = CONTROLE.exec(r);
        if (c) {
          (r.match(NUMMER) || []).forEach(function (nr) {
            if (!(nr in controles)) controles[nr] = [];
            controles[nr].push(c[1]);
          });
        }
      });
      if (oordeel === "open") {
        while (inhoud.length && !inhoud[inhoud.length - 1].trim()) inhoud.pop();
        while (inhoud.length && !inhoud[0].trim()) inhoud.shift();
        regels.push(kopVanBlok(deel.als, vragen), ">");
        inhoud.forEach(function (r) { regels.push(r.trim() ? "> " + r : ">"); });
        regels.push("");
      } else {
        regels = regels.concat(inhoud);
      }
    });
    var tekst = stripNl(nummerRegels(regels).join("\n")).replace(/\n{3,}/g, "\n\n");

    var alle = data.maatregelen.maatregelen;
    var eigen = alle.filter(function (m) { return m.thema === domein.naam; });
    var eigenIds = eigen.map(function (m) { return m.id; });
    var overheid = eigen.filter(function (m) { return m.soort === "overheid"; }).map(function (m) { return m.id; });
    var titels = {};
    alle.forEach(function (m) { titels[m.id] = m.titel; });
    var beantwoord = [];
    data.profiel.vragen.forEach(function (v) {
      var a = antwoordenVan(profiel, v.id);
      if (a !== null) beantwoord.push([v.vraag, a.map(function (x) { return label(vragen, v.id, x); }).join(", ")]);
    });

    var uit = ["# " + steen.titel, ""];
    var titelblad = [
      "| | |", "|---|---|",
      "| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *" + domein.naam + "* |",
      "| Status | Concept, vast te stellen door de organisatie |",
      "| Eigenaar | [[eigenaar van dit beleid: de manager die dit beleid uitvoert en laat naleven]] |",
      "| Vaststeller | [[vaststeller: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur]] |",
      "| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |"
    ];
    titelblad.forEach(function (r) { uit.push(vulVelden(r, velden)); });
    uit.push("");
    if (steen.samenvatting) uit.push("**In het kort.** " + steen.samenvatting, "");
    var koppen = [];
    steen.delen.forEach(function (deel) {
      deel.regels.forEach(function (r) { var m = HOOFDSTUK.exec(r); if (m) koppen.push(m); });
    });
    var onderwerpen = koppen.slice(VOOR, koppen.length - ACHTER);
    if (onderwerpen.length) {
      uit.push("**Onderwerpen.** " + onderwerpen.map(function (m) { return m[1] + ". " + m[2]; }).join("; ") + ".", "");
    }
    if (beantwoord.length) {
      uit.push("Opgesteld voor dit profiel: " + beantwoord.map(function (b) { return b[0] + " " + b[1]; }).join("; ") + ".");
    } else {
      uit.push("Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.");
    }
    uit.push("", tekst, "", "## Bijlage A: BIO 2.0-maatregelen", "");
    uit.push("De maatregelen van dit domein (" + eigen.length + ", waarvan " + overheid.length + " overheidsmaatregelen), waar dit " +
             "stuk ze invult en welke controle ze aantoont. Nummers volgens " + data.maatregelen.versie + "; de " +
             "tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de " +
             "ISO 27002-beheersmaatregel.");
    uit.push("", "| Maatregel | Titel | Soort | In dit stuk | Controle |", "|---|---|---|---|---|");
    eigen.forEach(function (m) {
      var soort = m.soort === "overheid" ? "overheidsmaatregel" : "ISO-beheersmaatregel";
      uit.push("| " + m.id + " | " + m.titel + " | " + soort + " | " + (m.id in gedekt ? gedekt[m.id] : "niet ingevuld") + " | " +
               ((controles[m.id] || []).join(", ") || "geen") + " |");
    });
    var anders = Object.keys(gedekt).filter(function (nr) { return eigenIds.indexOf(nr) < 0; }).sort();
    if (anders.length) {
      uit.push("", "Daarnaast vult dit stuk maatregelen van andere domeinen mee in: " +
               anders.map(function (nr) { return nr + " (" + (titels[nr] || "?") + ")"; }).join(", ") + ".");
    }
    var woorden = {};
    (tekst.match(/[\w&]+/g) || []).forEach(function (w) { woorden[w] = true; });
    var gebruikt = Object.keys(data.afkortingen).sort().filter(function (k) { return woorden[k] === true; });
    if (gebruikt.length) {
      uit.push("", "## Bijlage B: Afkortingen", "", "| Afkorting | Betekenis |", "|---|---|");
      gebruikt.forEach(function (k) { uit.push("| " + k + " | " + data.afkortingen[k] + " |"); });
    }
    if (velden.length) {
      uit.push("", "## Nog in te vullen", "");
      velden.forEach(function (v) { uit.push("- **" + v[0] + "**" + (v[1] ? ": " + v[1] : "")); });
    }
    return { markdown: uit.join("\n") + "\n", gedekt: Object.keys(gedekt).sort(), controles: Object.keys(controles).sort(),
             eigen: eigenIds, overheid: overheid, waar: gedekt, controle_per: controles };
  }

  function profielzin(data, profiel) {
    var vragen = {}, beantwoord = [];
    data.profiel.vragen.forEach(function (v) { vragen[v.id] = v; });
    data.profiel.vragen.forEach(function (v) {
      var a = antwoordenVan(profiel, v.id);
      if (a !== null) beantwoord.push(v.vraag + " " + a.map(function (x) { return label(vragen, v.id, x); }).join(", "));
    });
    return beantwoord.length ? "Opgesteld voor dit profiel: " + beantwoord.join("; ") + "."
      : "Zonder profiel: tekst die van een contextvraag afhangt, telt mee.";
  }

  function cellen(regel) {
    if (regel.indexOf("> ") === 0) regel = regel.slice(2);
    return regel.trim().replace(/^\|+/, "").replace(/\|+$/, "").split("|").map(function (c) { return c.trim(); });
  }

  function veldenVan(markdown) {
    var i = markdown.indexOf(LIJSTKOP);
    if (i < 0) return [];
    var lijst = markdown.slice(i + LIJSTKOP.length).split("\n## ")[0];
    return lijst.split("\n").filter(function (r) { return r.indexOf("- **") === 0; })
      .map(function (r) { return r.slice(4).split("**")[0]; });
  }

  // Spiegel van overzichten in tools/bouw_beleidsset.py.
  function overzichten(data, profiel, stukken) {
    var domeinen = {}, thema = {};
    data.profiel.domeinen.forEach(function (d) { domeinen[d.id] = d.naam; });
    data.bouwstenen.forEach(function (s) { thema[domeinen[s.domein]] = s; });
    var zin = profielzin(data, profiel);

    var m = ["# Maatregelenoverzicht", "", zin, "",
      "Per BIO 2.0-maatregel het beleidsstuk dat hem invult, het hoofdstuk waar dat gebeurt en de controle die de " +
      "naleving aantoont. Nummers volgens " + data.maatregelen.versie + ". Komt een maatregel ook in een ander stuk " +
      "terug, dan staat dat in de laatste kolom.", "",
      "| Maatregel | Titel | Soort | Beleidsstuk | Hoofdstuk | Controle | Ook in |", "|---|---|---|---|---|---|---|"];
    data.maatregelen.maatregelen.slice().sort(function (a, b) { return a.id < b.id ? -1 : a.id > b.id ? 1 : 0; }).forEach(function (mr) {
      var steen = thema[mr.thema];
      if (!steen) return;
      var stuk = stukken[steen.domein];
      var ook = data.bouwstenen.filter(function (s) { return s !== steen && mr.id in stukken[s.domein].waar; })
        .map(function (s) { return s.titel; });
      m.push("| " + mr.id + " | " + mr.titel + " | " + (mr.soort === "overheid" ? "overheid" : "ISO") + " | " + steen.titel + " | " +
        (mr.id in stuk.waar ? stuk.waar[mr.id] : "niet ingevuld") + " | " +
        ((stuk.controle_per[mr.id] || []).join(", ") || "geen") + " | " + ook.join(", ") + " |");
    });

    var v = ["# Invoeren: wat er nog moet gebeuren", "", zin, "",
      "Een vastgesteld beleid werkt pas als de organisatie het inricht. Deze lijst zet per stuk op een rij wat " +
      "daarvoor nodig is: wat de organisatie inricht, welke controles zij gaat uitvoeren en wat zij nog moet " +
      "invullen. Een plan met volgorde, eigenaar per thema en urenraming staat in " +
      "[BIO 2.0 invoeren](" + WEBPLEK + "bio2-implementeren/).", "",
      "## Voor de hele set", "",
      "- Wijs per stuk de eigenaar aan en laat het stuk vaststellen.",
      "- Richt één registratie van controles in: per controle de uitvoerder, de frequentie, het bewijs en de uitkomst.",
      "- Richt het risicoregister in voor afwijkingen en bevindingen, met een risico-eigenaar die restrisico's accepteert.",
      "- Zet alle controles in een jaarkalender, zodat elke controle op tijd wordt uitgevoerd."];
    data.bouwstenen.forEach(function (s, i) {
      var md = stukken[s.domein].markdown;
      var rijen = md.split("\n").filter(function (r) { return RIJ.test(r); }).map(cellen);
      v.push("", "## " + (i + 1) + ". " + s.titel, "");
      if (s.invoeren && s.invoeren.length) {
        v.push("**Inrichten**", "");
        s.invoeren.forEach(function (a) { v.push("- " + a); });
        v.push("");
      }
      if (rijen.length) {
        v.push("**Controles inrichten (" + rijen.length + ")**", "", "| Nr | Controle | Uitvoerder | Frequentie |", "|---|---|---|---|");
        rijen.forEach(function (c) { v.push("| " + c[0] + " | " + c[1] + " | " + c[2] + " | " + c[3] + " |"); });
        v.push("");
      }
      var velden = veldenVan(md);
      v.push("**Nog in te vullen (" + velden.length + ").** " + (velden.length ? velden.join("; ") + "." : "Niets."));
    });
    return { maatregelen: m.join("\n") + "\n", invoeren: v.join("\n") + "\n" };
  }

  function genereer(data, profiel) {
    var uit = {};
    data.bouwstenen.forEach(function (s) { uit[s.domein] = genereerStuk(s, data, profiel); });
    return uit;
  }

  var LIJSTKOP = "\n## Nog in te vullen\n";

  // Spiegel van vul_waarden in tools/bouw_beleidsset.py.
  function vulWaarden(markdown, waarden, herkomst) {
    var gevuld = [];
    Object.keys(waarden).sort().forEach(function (naam) {
      var waarde = String(waarden[naam]).trim();
      var doel = "**[" + naam + "]**";
      if (waarde && markdown.indexOf(doel) >= 0) {
        markdown = markdown.split(doel).join(waarde);
        gevuld.push(naam);
      }
    });
    if (!gevuld.length) return markdown;
    var i = markdown.indexOf(LIJSTKOP);
    if (i >= 0) {
      var voor = markdown.slice(0, i), lijst = markdown.slice(i + LIJSTKOP.length);
      var blijft = lijst.split("\n").filter(function (r) {
        return r.indexOf("- **") === 0 && gevuld.indexOf(r.slice(4).split("**")[0]) < 0;
      });
      markdown = voor.replace(/\n+$/, "") + "\n";
      if (blijft.length) markdown += LIJSTKOP + "\n" + blijft.join("\n") + "\n";
    }
    if (herkomst) {
      markdown += "\n## Herkomst van ingevulde waarden\n\n" +
        "Ingevuld uit een AI-voorstel (" + (herkomst.leverancier || "?") + ", model " + (herkomst.model || "?") + ", " +
        (herkomst.gemaakt || "?") + ", invoer sha256 " + String(herkomst.sha256 || "").slice(0, 12) + "): " +
        gevuld.join(", ") + ". Controleer elke waarde voordat je het stuk vaststelt.\n";
    }
    return markdown;
  }

  var api = { genereer: genereer, genereerStuk: genereerStuk, beoordeel: beoordeel, vulWaarden: vulWaarden,
              overzichten: overzichten };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else wereld.Beleidsset = api;
})(this);
