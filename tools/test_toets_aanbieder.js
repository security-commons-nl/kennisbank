// Tests op de beslislogica van de toets "Ben ik aanbieder onder de AI Act?"
// (governance/aanbieder-onder-de-ai-act).
//
// Zelfde opzet als test_toets_cbw.js: het script gaat uit de leesversie en draait in een vm met een
// minimale DOM. Wat hier bewaakt wordt is waar de toets zijn bestaansrecht aan ontleent: wie zelf een
// toepassing samenstelt is aanbieder, ook op een ingekocht platform; profilering sluit de uitzondering
// van art. 6 lid 3 uit; en art. 25 maakt een gebruiker alleen aanbieder van een hoog-risicosysteem.
//
// Draaien: node tools/test_toets_aanbieder.js

"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const PAGINA = path.join(__dirname, "..", "governance", "aanbieder-onder-de-ai-act", "index.html");

function laadScript() {
  const html = fs.readFileSync(PAGINA, "utf8");
  const m = html.match(/<script>([\s\S]*?)<\/script>/);
  if (!m) { throw new Error("geen <script> gevonden in " + PAGINA); }
  return m[1];
}

function maakContext() {
  const leeg = () => ({
    innerHTML: "", textContent: "", value: "", onclick: null, oninput: null, onchange: null,
    querySelectorAll: () => [], appendChild: () => {}
  });
  const opslag = {};
  const ctx = {
    document: {
      getElementById: () => leeg(),
      createElement: () => {
        const d = { _h: "" };
        Object.defineProperty(d, "textContent", {
          set(v) {
            d._h = String(v).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
          },
          get() { return d._h; }
        });
        Object.defineProperty(d, "innerHTML", { get() { return d._h; } });
        return d;
      },
      createRange: () => ({ selectNodeContents: () => {} })
    },
    window: {
      scrollTo: () => {},
      localStorage: {
        getItem: (k) => (k in opslag ? opslag[k] : null),
        setItem: (k, v) => { opslag[k] = String(v); },
        removeItem: (k) => { delete opslag[k]; }
      },
      getSelection: () => ({ removeAllRanges: () => {}, addRange: () => {} })
    },
    navigator: {},
    console
  };
  ctx.globalThis = ctx;
  return vm.createContext(ctx);
}

const ctx = maakContext();
vm.runInContext(laadScript(), ctx, { filename: "toets-aanbieder.js" });

// `antwoord` en `bewijs` zijn in het script met var gedeclareerd, dus globale eigenschappen van de
// context. Het script leest ze via de naam, dus we vullen de bestaande objecten in plaats van ze te
// vervangen.
function zet(obj, waarden) {
  Object.keys(obj).forEach((k) => { delete obj[k]; });
  Object.assign(obj, waarden);
}

let fouten = 0;
let gedaan = 0;

function gelijk(werkelijk, verwacht, wat) {
  gedaan++;
  const ok = JSON.stringify(werkelijk) === JSON.stringify(verwacht);
  if (!ok) {
    fouten++;
    console.error("  FOUT  " + wat + "\n        verwacht: " + JSON.stringify(verwacht) +
                  "\n        kreeg:    " + JSON.stringify(werkelijk));
  } else {
    console.log("  ok    " + wat);
  }
}

function bevat(lijst, stuk, wat) {
  gedaan++;
  const ok = lijst.some((r) => r.indexOf(stuk) !== -1);
  if (!ok) {
    fouten++;
    console.error("  FOUT  " + wat + "\n        geen regel met: " + stuk +
                  "\n        wel: " + JSON.stringify(lijst));
  } else {
    console.log("  ok    " + wat);
  }
}

function bevatNiet(lijst, stuk, wat) {
  gedaan++;
  const ok = !lijst.some((r) => r.indexOf(stuk) !== -1);
  if (!ok) {
    fouten++;
    console.error("  FOUT  " + wat + "\n        had geen regel mogen bevatten met: " + stuk);
  } else {
    console.log("  ok    " + wat);
  }
}

// Elk beantwoord punt krijgt standaard een onderbouwing, zodat een test over de logica niet struikelt
// over een leeg veld.
function vul(antwoorden, opties) {
  const zonder = (opties && opties.zonderOnderbouwing) || [];
  const b = {};
  Object.keys(antwoorden).forEach((nr) => {
    if (zonder.indexOf(nr) === -1) { b[nr] = "onderbouwing bij " + nr; }
  });
  zet(vm.runInContext("antwoord", ctx), antwoorden);
  zet(vm.runInContext("bewijs", ctx), b);
}

const INGEKOCHT = vm.runInContext("INGEKOCHT", ctx);
const SAMENGESTELD = vm.runInContext("SAMENGESTELD", ctx);
const ONTWIKKELD = vm.runInContext("ONTWIKKELD", ctx);

function uitkomst() {
  return ctx.bepaalUitkomst(ctx.stand(), ctx.openPunten()).soort;
}

// Een interne assistent op een ingekocht chatplatform, met eigen instructies en kennisbron.
const ASSISTENT = {
  "1.1": "ja", "2.1": SAMENGESTELD, "2.2": "nee",
  "3.1": "nee", "3.2": "nee", "3.3": "nee", "5.1": "nee"
};

// Een ingekocht product, gebruikt zoals geleverd, buiten bijlage III.
const PRODUCT = {
  "1.1": "ja", "2.1": INGEKOCHT, "3.1": "nee", "3.2": "nee", "3.3": "nee", "5.1": "nee"
};

console.log("\nRol: samenstellen maakt aanbieder");
vul(ASSISTENT);
gelijk(ctx.standRol().rol, "aanbieder", "een assistent op een ingekocht platform maakt de gemeente aanbieder");
gelijk(uitkomst(), "aanbieder-laag", "zonder bijlage III blijft het bij aanbieder zonder hoog risico");

vul(Object.assign({}, ASSISTENT, { "2.1": ONTWIKKELD }));
gelijk(ctx.standRol().rol, "aanbieder", "zelf laten ontwikkelen maakt ook aanbieder");

vul(PRODUCT);
gelijk(ctx.standRol().rol, "gebruiker", "ingekocht en gebruikt zoals geleverd blijft gebruiker");
gelijk(uitkomst(), "gebruiker-laag", "en zonder bijlage III is dat gebruiker zonder hoog risico");

console.log("\nRisico: bijlage III, profilering en de uitzondering");
vul(Object.assign({}, ASSISTENT, { "3.1": "ja", "3.4": "nee", "3.5": "nee" }));
gelijk(ctx.standRisico(), "hoog", "beoordelen van recht op een voorziening is hoog risico");
gelijk(uitkomst(), "aanbieder-hoog", "zelf samengesteld en hoog risico is de zware uitkomst");

vul(Object.assign({}, ASSISTENT, { "3.1": "ja", "3.4": "ja", "3.5": "ja" }));
gelijk(ctx.standRisico(), "hoog", "met profilering geldt de uitzondering niet, ook niet als 3.5 ja is");
bevatNiet(ctx.openPunten(), "3.5", "vraag 3.5 verdwijnt bij profilering en telt niet mee");

vul(Object.assign({}, ASSISTENT, { "3.1": "ja", "3.4": "nee", "3.5": "ja" }));
gelijk(ctx.standRisico(), "uitzondering", "een voorbereidende taak zonder profilering kan onder art. 6 lid 3 vallen");
gelijk(uitkomst(), "uitzondering", "en dat krijgt een eigen uitkomst die om onderbouwing vraagt");

vul(Object.assign({}, ASSISTENT, { "3.2": "ja", "3.4": "nee", "3.5": "nee" }));
gelijk(ctx.standRisico(), "hoog", "werving en selectie is ook hoog risico");

vul(ASSISTENT);
bevatNiet(ctx.openPunten(), "3.4", "zonder bijlage III verschijnen profilering en uitzondering niet");

console.log("\nArt. 25: van gebruiker naar aanbieder");
vul(Object.assign({}, PRODUCT, { "3.1": "ja", "3.4": "nee", "3.5": "nee", "4.1": "nee", "4.2": "ja" }));
gelijk(ctx.standRol(), { rol: "aanbieder", route: "art25" }, "een ingekocht model inzetten voor een hoog-risicodoel maakt aanbieder");
gelijk(uitkomst(), "aanbieder-hoog", "met de zware uitkomst");

vul(Object.assign({}, PRODUCT, { "3.1": "ja", "3.4": "nee", "3.5": "nee", "4.1": "ja", "4.2": "nee" }));
gelijk(ctx.standRol().rol, "aanbieder", "eigen naam op een hoog-risicosysteem maakt aanbieder");

vul(Object.assign({}, PRODUCT, { "3.1": "ja", "3.4": "nee", "3.5": "nee", "4.1": "nee", "4.2": "nee" }));
gelijk(uitkomst(), "gebruiker-hoog", "een hoog-risicoproduct gebruikt zoals bedoeld maakt gebruiksverantwoordelijke");

vul(PRODUCT);
bevatNiet(ctx.openPunten(), "4.1", "zonder bijlage III verschijnen de art. 25-vragen niet");

console.log("\nGeen AI-systeem");
vul({ "1.1": "nee" }, {});
gelijk(uitkomst(), "geenai", "een vaste rekenregel valt buiten de AI Act");
gelijk(ctx.openPunten(), [], "en de overige vragen tellen dan niet mee");

console.log("\nGeen conclusie zonder volledige onderbouwing");
vul(Object.assign({}, ASSISTENT, { "3.1": "onbekend" }));
gelijk(uitkomst(), "jurist", "onbekend op bijlage III geeft geen conclusie");
bevat(ctx.openPunten(), "3.1 staat op onbekend", "en komt terug als open punt");
bevat(ctx.openPunten(), "3.4 is niet beantwoord", "en haalt de vervolgvragen erbij");

vul(Object.assign({}, ASSISTENT, { "2.1": "weet ik niet" }));
gelijk(uitkomst(), "jurist", "onbekend hoe de toepassing ontstond geeft geen conclusie");

vul(ASSISTENT, { zonderOnderbouwing: ["2.1"] });
bevat(ctx.openPunten(), "2.1 heeft geen onderbouwing", "ontbrekende onderbouwing is een open punt");
gelijk(uitkomst(), "jurist", "zonder onderbouwing geen classificatiebesluit");

vul({ "1.1": "ja" });
gelijk(uitkomst(), "jurist", "een half ingevulde toets concludeert niets");

console.log("\nAanvullende regels");
vul(Object.assign({}, ASSISTENT, { "2.2": "ja", "5.1": "ja" }));
const extra = ctx.extraRegels(ctx.stand());
bevat(extra, "aan andere organisaties", "delen met andere organisaties wordt benoemd");
bevat(extra, "art. 50", "contact met inwoners haalt de transparantieplicht erbij");

vul(Object.assign({}, PRODUCT, { "2.2": "ja" }));
gelijk(ctx.stand().deelt, false, "een verborgen antwoord op 2.2 telt niet mee bij een ingekocht product");

console.log("\nDossier");
vul(Object.assign({}, ASSISTENT, { "3.1": "ja", "3.4": "nee", "3.5": "nee" }));
const u = ctx.bepaalUitkomst(ctx.stand(), ctx.openPunten());
const md = ctx.maakDossier(u, ctx.extraRegels(ctx.stand()), ctx.openPunten()).split("\n");
gelijk(md[0], "# Classificatiebesluit AI Act", "dossier begint met een kop");
bevat(md, "Uitkomst: Aanbieder van een hoog-risicosysteem", "dossier noemt de uitkomst");
bevat(md, "- Conformiteitsbeoordeling en CE-markering (art. 43 en 48)", "dossier noemt de plichten");
bevat(md, "- Antwoord: " + SAMENGESTELD, "dossier neemt de antwoorden over");
bevat(md, "- Juridisch getoetst door:", "dossier heeft een vaststellingsblok");
bevatNiet(md, "## Word je aanbieder van andermans systeem?", "een stap zonder zichtbare vragen staat niet in het dossier");

console.log("\n" + (fouten === 0
  ? gedaan + " controles, alles goed."
  : gedaan + " controles, " + fouten + " fout."));
process.exit(fouten === 0 ? 0 : 1);
