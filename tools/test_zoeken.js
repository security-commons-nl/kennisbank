// Toetst het zoekvak van de voorpagina zoals een lezer het gebruikt: het echte script uit de
// gebouwde index.html, op de echte stukken en de echte bronnen van anderen.
//
// Draaien: node tools/test_zoeken.js   (na python tools/build.py)
//
// Aanleiding (25-09-2026): een ISO die "iets van de VNG over beleid" zocht, vond niets, en na de
// eerste bouw vond "continuiteit" iets anders dan "continuïteit" en gaf "privacy" 119 treffers.
// Deze test houdt vast wat er toen is afgesproken.
'use strict';
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const ontsnap = s => s.replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>').replace(/&amp;/g, '&');

function element(attrs) {
  return { hidden: false, textContent: '', value: '', _h: {},
    getAttribute: n => (n in attrs ? attrs[n] : null),
    addEventListener(soort, f) { this._h[soort] = f; } };
}

const kaarten = [...html.matchAll(/<a class="item" href="[^"]*" data-vak="[^"]*" data-zoek="([^"]*)" data-barrieres="([^"]*)"/g)]
  .map(m => element({ 'data-zoek': ontsnap(m[1]), 'data-barrieres': ontsnap(m[2]) }));
const bronnen = [...html.matchAll(/<li data-zoek="([^"]*)"><a href="([^"]*)">([^<]*)<\/a>/g)]
  .map(m => Object.assign(element({ 'data-zoek': ontsnap(m[1]) }), { titel: ontsnap(m[3]) }));
const syn = (html.match(/<script type="application\/json" id="synoniemen">([\s\S]*?)<\/script>/) || [])[1] || '[]';
const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).find(s => s.includes('function past'));

let fouten = 0;
function toets(naam, ok, extra) {
  console.log((ok ? '  ok   ' : '  FOUT ') + naam + (ok || !extra ? '' : '  (' + extra + ')'));
  if (!ok) fouten++;
}

toets('het zoekscript staat in de pagina', !!script);
toets('er staan bronnen van anderen in de pagina', bronnen.length > 300, bronnen.length);

const els = {
  filters: element({}), zoek: element({}), barriere: element({}), telling: element({}),
  'filter-leeg': element({}), 'bij-anderen-kop': element({}), 'bij-anderen-uitleg': element({}),
  synoniemen: Object.assign(element({}), { textContent: syn }),
  'direct-te-lezen': Object.assign(element({}), { querySelectorAll: () => kaarten }),
  'bij-anderen': Object.assign(element({}), { querySelectorAll: () => bronnen }),
};
new Function('document', script)({ getElementById: id => els[id] || null });

function zoek(term, barriere) {
  els.zoek.value = term;
  els.barriere.value = barriere || '';
  els.zoek._h.input();
  return { eigen: kaarten.filter(k => !k.hidden).length, anders: bronnen.filter(b => !b.hidden) };
}
const titels = r => r.anders.map(b => b.titel.toLowerCase());

// Het scenario waar het om begon.
let r = zoek('vng beleid');
toets('"vng beleid" vindt het sjabloon strategisch beleid van de IBD',
  titels(r).some(t => t.includes('template strategisch informatiebeveiligings')), r.anders.length);
toets('zonder zoekterm staan de bronnen van anderen niet open', zoek('').anders.length === 0);

// Accenten, koppeltekens, hoofdletters.
toets('continuiteit en continuïteit geven hetzelfde',
  zoek('continuiteit').anders.length === zoek('continuïteit').anders.length && zoek('continuiteit').anders.length > 0);
toets('backup en back-up geven hetzelfde',
  zoek('backup').anders.length === zoek('back-up').anders.length && zoek('backup').anders.length > 0);
toets('hoofdletters tellen niet',
  zoek('DPIA').anders.length === zoek('dpia').anders.length && zoek('dpia').anders.length > 0);

// Synoniemen.
toets('cbw vindt de stukken over de Cyberbeveiligingswet',
  titels(zoek('cbw')).some(t => t.includes('cyberbeveiligingswet')));
toets('mfa vindt de stukken over 2FA', titels(zoek('mfa')).some(t => t.includes('2fa')));
toets('awareness vindt bewustwording', titels(zoek('awareness')).some(t => t.includes('bewustwording')));

// Geen vervuiling: een gewoon woord mag niet een hele catalogus opleveren.
r = zoek('privacy');
toets('privacy geeft niet alle stukken van CIP', r.anders.length < 100, r.anders.length);
r = zoek('gemeenten');
toets('gemeenten geeft niet alle stukken van de IBD', r.anders.length < 150, r.anders.length);
r = zoek('ai');
toets('ai vindt de AI-stukken, maar niet elk woord met die letters erin',
  r.anders.length > 0 && r.anders.every(b => /(^|[^a-z])ai/i.test(b.titel + ' ' + b.getAttribute('data-zoek'))),
  r.anders.map(b => b.titel).join(' | '));

// Samenwerking met het barrierefilter.
toets('met een barriere gekozen blijven de bronnen van anderen weg', zoek('beleid', 'crisis').anders.length === 0);

console.log(fouten ? `\n${fouten} fout(en).` : '\nAlles goed.');
process.exit(fouten ? 1 : 0);
