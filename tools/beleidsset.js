// Generator van de beleidsset: dezelfde rekenregel als genereer_stuk in tools/bouw_beleidsset.py.
// Wijzig ze samen; tools/test_beleidsset.py vergelijkt de uitvoer van beide op een reeks profielen.
// Werkt in de browser (window.Beleidsset) en in node (module.exports).
(function (wereld) {
  "use strict";
  var TAG = /\[(\d\.\d{2}\.\d{2}(?:,\s*\d\.\d{2}\.\d{2})*)\]/g;
  var VELD = /\[\[([^\]:]+?)(?::\s*([^\]]+?))?\]\]/g;

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
    var regels = [], velden = [], gedekt = {}, volgorde = [];
    var kop = steen.titel;
    steen.delen.forEach(function (deel) {
      var oordeel = deel.als === null ? "ja" : beoordeel(deel.als, profiel);
      if (oordeel === "nee") return;
      var inhoud = deel.regels.map(function (r) { return vulVelden(r, velden); });
      deel.regels.forEach(function (r) {
        if (r.charAt(0) === "#") kop = r.replace(/^#+/, "").trim();
        r.replace(TAG, function (_, nrs) {
          nrs.split(/,\s*/).forEach(function (nr) {
            if (!(nr in gedekt)) { gedekt[nr] = kop; volgorde.push(nr); }
          });
          return _;
        });
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
    var tekst = stripNl(regels.join("\n")).replace(/\n{3,}/g, "\n\n");

    var alle = data.maatregelen.maatregelen;
    var eigen = alle.filter(function (m) { return m.thema === domein.naam && m.soort === "overheid"; });
    var eigenIds = eigen.map(function (m) { return m.id; });
    var titels = {};
    alle.forEach(function (m) { titels[m.id] = m.titel; });
    var beantwoord = [];
    data.profiel.vragen.forEach(function (v) {
      var a = antwoordenVan(profiel, v.id);
      if (a !== null) beantwoord.push([v.vraag, a.map(function (x) { return label(vragen, v.id, x); }).join(", ")]);
    });

    var uit = ["# " + steen.titel, ""];
    uit.push("Beleid informatiebeveiliging, BIO 2.0-domein *" + domein.naam + "*. Status: concept, vast te " +
             "stellen door de organisatie zelf.");
    uit.push("");
    if (beantwoord.length) {
      uit.push("Opgesteld voor dit profiel: " + beantwoord.map(function (b) { return b[0] + " " + b[1]; }).join("; ") + ".");
    } else {
      uit.push("Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.");
    }
    uit.push("", tekst, "", "## Bijlage: BIO 2.0-maatregelen", "");
    uit.push("De overheidsmaatregelen van dit domein (" + eigen.length + ") en waar dit stuk ze invult. Nummers volgens " +
             data.maatregelen.versie + "; de tekst van de maatregel staat bij het CIP.");
    uit.push("", "| Maatregel | Titel | In dit stuk |", "|---|---|---|");
    eigen.forEach(function (m) {
      uit.push("| " + m.id + " | " + m.titel + " | " + (m.id in gedekt ? gedekt[m.id] : "niet ingevuld") + " |");
    });
    var thema = alle.filter(function (m) { return m.thema === domein.naam; }).map(function (m) { return m.id; });
    var iso = Object.keys(gedekt).filter(function (nr) { return thema.indexOf(nr) >= 0 && eigenIds.indexOf(nr) < 0; }).sort();
    if (iso.length) {
      uit.push("", "Ook ingevuld, ISO-beheersmaatregelen van dit domein zonder overheidsmaatregel: " +
               iso.map(function (nr) { return nr + " (" + (titels[nr] || "?") + ")"; }).join(", ") + ".");
    }
    var anders = Object.keys(gedekt).filter(function (nr) { return thema.indexOf(nr) < 0; }).sort();
    if (anders.length) {
      uit.push("", "Daarnaast vult dit stuk maatregelen van andere domeinen mee in: " +
               anders.map(function (nr) { return nr + " (" + (titels[nr] || "?") + ")"; }).join(", ") + ".");
    }
    if (velden.length) {
      uit.push("", "## Nog in te vullen", "");
      velden.forEach(function (v) { uit.push("- **" + v[0] + "**" + (v[1] ? ": " + v[1] : "")); });
    }
    return { markdown: uit.join("\n") + "\n", gedekt: Object.keys(gedekt).sort(), eigen: eigenIds };
  }

  function genereer(data, profiel) {
    var uit = {};
    data.bouwstenen.forEach(function (s) { uit[s.domein] = genereerStuk(s, data, profiel); });
    return uit;
  }

  var api = { genereer: genereer, genereerStuk: genereerStuk, beoordeel: beoordeel };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else wereld.Beleidsset = api;
})(this);
