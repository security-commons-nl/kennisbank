// Tests op de beslislogica van de Cbw-toets (governance/val-ik-onder-de-cbw).
//
// De toets rekent in de browser, dus de logica staat in een <script> in de leesversie. Deze test
// haalt dat script eruit en draait het in een vm met een minimale DOM eromheen, zodat de criteria
// getest worden zonder browser. Wat hier bewaakt wordt is de kern: de vier criteria zijn cumulatief,
// criterium 3 kent drie alternatieve routes waarvan er een volstaat, en criterium 4 vraagt naast
// besluitbevoegdheid ook een EU-grondslag. Die laatste is de nuance waar de toets zijn bestaansrecht
// aan ontleent; zonder test zou een herschrijving hem stilletjes kunnen omdraaien.
//
// Draaien: node tools/test_toets_cbw.js

"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const PAGINA = path.join(__dirname, "..", "governance", "val-ik-onder-de-cbw", "index.html");

function laadScript() {
  const html = fs.readFileSync(PAGINA, "utf8");
  const m = html.match(/<script>([\s\S]*?)<\/script>/);
  if (!m) { throw new Error("geen <script> gevonden in " + PAGINA); }
  return m[1];
}

// De kleinst mogelijke DOM: genoeg om het script te laten laden zonder browser.
function maakContext() {
  const leeg = () => {
    const el = {
      innerHTML: "", textContent: "", value: "", onclick: null, oninput: null, onchange: null,
      querySelectorAll: () => [], appendChild: () => {}
    };
    return el;
  };
  const opslag = {};
  const ctx = {
    document: {
      getElementById: () => leeg(),
      createElement: () => {
        const d = { _h: "" };
        Object.defineProperty(d, "textContent", {
          set(v) {
            d._h = String(v)
              .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
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
vm.runInContext(laadScript(), ctx, { filename: "toets-cbw.js" });

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

// Zet antwoorden klaar. Elk beantwoord punt krijgt standaard een bewijsstuk, zodat een test die
// over de criteria gaat niet struikelt over ontbrekend bewijs.
function vul(antwoorden, opties) {
  const zonderBewijs = (opties && opties.zonderBewijs) || [];
  ctx.antwoord = {};
  ctx.bewijs = {};
  Object.keys(antwoorden).forEach((nr) => {
    ctx.antwoord[nr] = antwoorden[nr];
    if (zonderBewijs.indexOf(nr) === -1) { ctx.bewijs[nr] = "bewijsstuk bij " + nr; }
  });
}

const VOLLEDIG_IN_SCOPE = {
  "1.1": "ja", "1.2": "ja",
  "2.1": "openbaar lichaam",
  "3.1": "ja", "3.2": "ja", "3.3": "ja",
  "4.1": "ja", "4.2": "gedelegeerd", "4.3": "ja", "4.4": "ja", "4.5": "ja",
  "5.1": "nee"
};

function uitkomst() {
  return ctx.bepaalUitkomst(ctx.stand(), ctx.openPunten()).soort;
}

console.log("\nCriteria afzonderlijk");
vul(VOLLEDIG_IN_SCOPE);
gelijk(ctx.stand(), { c1: "ja", c2: "ja", c3: "ja", c4: "ja", c5: "nee" },
  "volledig ingevulde uitvoeringsorganisatie voldoet aan alle criteria");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "1.2": "nee" }));
gelijk(ctx.standC1(), "nee", "criterium 1 valt om zodra een van beide vragen nee is");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "2.1": "gemeenschappelijk orgaan", "2.2": "ja" }));
gelijk(ctx.standC2(), "ja", "zonder eigen rechtspersoonlijkheid telt optreden namens een deelnemer");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "2.1": "gemeenschappelijk orgaan", "2.2": "nee" }));
gelijk(ctx.standC2(), "nee", "geen rechtspersoonlijkheid en niet namens een ander bevoegd");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "3.1": "nee", "3.2": "nee", "3.3": "ja" }));
gelijk(ctx.standC3(), "ja", "criterium 3 heeft drie routes; een ja volstaat");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "3.1": "nee", "3.2": "nee", "3.3": "nee" }));
gelijk(ctx.standC3(), "nee", "criterium 3 valt pas om als alle drie de routes nee zijn");

console.log("\nCriterium 4: besluitbevoegdheid en EU-grondslag zijn cumulatief");
vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "4.3": "nee" }));
gelijk(ctx.standC4(), "nee", "Awb-besluiten zonder EU-grondslag laten criterium 4 niet slagen");
gelijk(uitkomst(), "niet", "en dat maakt de uitkomst niet in scope");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "4.4": "nee" }));
gelijk(ctx.standC4(), "nee", "uitgesloten grensoverschrijdend gevolg laat criterium 4 niet slagen");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "4.2": "in mandaat" }));
gelijk(uitkomst(), "wel", "mandaat is geen grond om buiten de reikwijdte te blijven");

console.log("\nVervolgvragen verschijnen alleen als ze ertoe doen");
vul({ "1.1": "ja", "1.2": "ja", "2.1": "openbaar lichaam", "3.1": "ja", "3.2": "ja", "3.3": "ja",
      "4.1": "nee", "4.5": "ja", "5.1": "nee" });
gelijk(ctx.standC4(), "nee", "geen Awb-besluiten laat criterium 4 vallen");
bevatNiet(ctx.openPunten(), "4.3", "de EU-vragen tellen niet mee als er geen besluiten worden genomen");
gelijk(uitkomst(), "niet", "strategisch samenwerkingsverband valt buiten scope");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "2.1": "openbaar lichaam" }));
bevatNiet(ctx.openPunten(), "2.2", "vraag 2.2 telt niet mee bij een vorm met rechtspersoonlijkheid");

console.log("\nUitkomsten");
vul(VOLLEDIG_IN_SCOPE);
gelijk(uitkomst(), "wel", "alles voldaan en geen uitzondering geeft wel in scope");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "2.1": "centrumregeling" }));
gelijk(uitkomst(), "centrum", "een centrumregeling krijgt een eigen uitkomst");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "5.1": "ja" }));
gelijk(uitkomst(), "jurist", "een mogelijke uitzondering gaat naar juridisch advies");

vul(Object.assign({}, VOLLEDIG_IN_SCOPE, { "4.3": "onbekend" }));
gelijk(uitkomst(), "jurist", "onbekend op een beslissende vraag geeft geen conclusie");
bevat(ctx.openPunten(), "4.3 staat op onbekend", "en komt terug als open punt");

vul(VOLLEDIG_IN_SCOPE, { zonderBewijs: ["3.2"] });
bevat(ctx.openPunten(), "3.2 heeft geen bewijsstuk", "ontbrekend bewijs is een open punt");
gelijk(uitkomst(), "jurist", "zonder onderbouwing geen harde conclusie");

vul({ "1.1": "ja" });
bevat(ctx.openPunten(), "5.1 is niet beantwoord", "onbeantwoorde vragen komen terug als open punt");
gelijk(uitkomst(), "jurist", "een half ingevulde toets concludeert niets");

console.log("\nDossier");
vul(VOLLEDIG_IN_SCOPE);
const md = ctx.maakDossier("Dit wijst op: wel in scope", ctx.openPunten());
gelijk(md.indexOf("# Toets Cyberbeveiligingswet") === 0, true, "dossier begint met een kop");
bevat(md.split("\n"), "Uitkomst: Dit wijst op: wel in scope", "dossier noemt de uitkomst");
bevat(md.split("\n"), "- Antwoord: gedelegeerd", "dossier neemt de antwoorden over");
bevat(md.split("\n"), "- Juridisch getoetst door:", "dossier heeft een vaststellingsblok");

console.log("\n" + (fouten === 0
  ? gedaan + " controles, alles goed."
  : gedaan + " controles, " + fouten + " fout."));
process.exit(fouten === 0 ? 0 : 1);
