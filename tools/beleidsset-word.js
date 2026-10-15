// Word-bestand (.docx) uit de markdown van de beleidsset: spiegel van tools/beleidsset_word.py.
// Wijzig ze samen; tools/test_beleidsset.py vergelijkt de onderdelen die beide maken.
// Werkt in de browser (window.BeleidssetWord) en in node (module.exports).
(function (wereld) {
  "use strict";
  var INLINE = /\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`|\[([^\]]+)\]\((https?:[^)\s]+|[^)\s]+)\)/g;
  var STIJLEN = { 1: "Title", 2: "Heading1", 3: "Heading2", 4: "Heading3" };
  var LIJST = /^(- |\d+\. )/;

  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

  function run(tekst, eigen) {
    if (!tekst) return "";
    var rpr = eigen ? "<w:rPr>" + eigen + "</w:rPr>" : "";
    return "<w:r>" + rpr + '<w:t xml:space="preserve">' + esc(tekst) + "</w:t></w:r>";
  }

  function runs(tekst, basis) {
    basis = basis || "";
    var uit = [], pos = 0, m, re = new RegExp(INLINE.source, "g");
    while ((m = re.exec(tekst)) !== null) {
      uit.push(run(tekst.slice(pos, m.index), basis));
      if (m[1] !== undefined) uit.push(runs(m[1], basis + "<w:b/>"));
      else if (m[2] !== undefined) uit.push(runs(m[2], basis + "<w:i/>"));
      else if (m[3] !== undefined) uit.push(run(m[3], basis + '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>'));
      else { uit.push(run(m[4], basis)); uit.push(run(" (" + m[5] + ")", basis)); }
      pos = m.index + m[0].length;
    }
    uit.push(run(tekst.slice(pos), basis));
    return uit.join("");
  }

  function alinea(stijl, inhoud) { return '<w:p><w:pPr><w:pStyle w:val="' + stijl + '"/></w:pPr>' + inhoud + "</w:p>"; }

  function cellen(regel) {
    return regel.trim().replace(/^\|+/, "").replace(/\|+$/, "").split("|").map(function (c) { return c.trim(); });
  }

  function tabel(rijen) {
    var kop = cellen(rijen[0]);
    // Kolombreedte naar de langste tekst in de kolom, tussen 8 en 60 tekens.
    var gewicht = kop.map(function (_, k) {
      var langst = 0;
      [rijen[0]].concat(rijen.slice(2)).forEach(function (r) { var c = cellen(r); langst = Math.max(langst, k < c.length ? c[k].length : 0); });
      return Math.min(Math.max(langst, 8), 60);
    });
    var som = gewicht.reduce(function (a, b) { return a + b; }, 0);
    var uit = ['<w:tbl><w:tblPr><w:tblStyle w:val="Tabel"/><w:tblW w:w="5000" w:type="pct"/></w:tblPr><w:tblGrid>' +
      gewicht.map(function (g) { return '<w:gridCol w:w="' + Math.floor(9638 * g / som) + '"/>'; }).join("") + "</w:tblGrid>"];
    [rijen[0]].concat(rijen.slice(2)).forEach(function (r, i) {
      var c = cellen(r).concat(kop.map(function () { return ""; })).slice(0, kop.length);
      if (i === 0 && !c.some(function (x) { return x; })) return;  // een lege kopregel, zoals boven het titelblad
      uit.push("<w:tr>" + (i === 0 ? "<w:trPr><w:tblHeader/></w:trPr>" : "") + c.map(function (x) {
        return '<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr>' + alinea("Tabeltekst", runs(x, i === 0 ? "<w:b/>" : "")) + "</w:tc>";
      }).join("") + "</w:tr>");
    });
    return uit.join("") + "</w:tbl>" + alinea("Tabeleinde", "");
  }

  function blokken(md, kader) {
    var regels = md.split("\n"), uit = [], i = 0;
    var tekststijl = kader ? "Kader" : "Normal", lijststijl = kader ? "Kaderlijst" : "Lijst";
    while (i < regels.length) {
      var r = regels[i];
      if (r.charAt(0) === ">") {
        var blok = [];
        while (i < regels.length && regels[i].charAt(0) === ">") { blok.push(regels[i].replace(/^> ?/, "")); i++; }
        uit.push(blokken(blok.join("\n"), true));
        continue;
      }
      var k = /^(#{1,4}) (.*)$/.exec(r);
      if (k) { uit.push(alinea(STIJLEN[k[1].length], runs(k[2]))); i++; continue; }
      if (r.charAt(0) === "|") {
        var rijen = [];
        while (i < regels.length && regels[i].charAt(0) === "|") { rijen.push(regels[i]); i++; }
        uit.push(tabel(rijen));
        continue;
      }
      if (LIJST.test(r)) {
        var genummerd = r.indexOf("- ") !== 0;
        var nummer = genummerd ? parseInt(r.split(".")[0], 10) : 1;
        var items = [];
        while (i < regels.length && /^(- |\d+\. |  +\S)/.test(regels[i])) {
          if (LIJST.test(regels[i])) items.push(regels[i].replace(LIJST, ""));
          else items[items.length - 1] += " " + regels[i].trim();
          i++;
        }
        items.forEach(function (item, n) {
          var teken = genummerd ? (nummer + n) + "." : "•";
          uit.push(alinea(lijststijl, run(teken) + "<w:r><w:tab/></w:r>" + runs(item)));
        });
        continue;
      }
      if (!r.trim()) { i++; continue; }
      var tekst = [];
      while (i < regels.length && regels[i].trim() && !/^(#|>|\||- |\d+\. )/.test(regels[i])) { tekst.push(regels[i]); i++; }
      uit.push(alinea(tekststijl, runs(tekst.join(" "))));
    }
    return uit.join("");
  }

  var NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" ' +
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"';
  var PAGINA = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" ' +
    'w:left="1134" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr>';
  var NIEUWE_PAGINA = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>';

  function documentXml(stukken) {
    var body = stukken.map(function (md) { return blokken(md.replace(/^\n+/, "").replace(/\n+$/, ""), false); }).join(NIEUWE_PAGINA);
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document ' + NS + "><w:body>" + body + PAGINA + "</w:body></w:document>";
  }

  function stijl(sid, naam, ppr, rpr, basis, soort) {
    basis = basis === undefined ? "Normal" : basis;
    return '<w:style w:type="' + (soort || "paragraph") + '" w:styleId="' + sid + '"><w:name w:val="' + naam + '"/>' +
      (basis ? '<w:basedOn w:val="' + basis + '"/>' : "") + "<w:qFormat/>" +
      (ppr ? "<w:pPr>" + ppr + "</w:pPr>" : "") + (rpr ? "<w:rPr>" + rpr + "</w:rPr>" : "") + "</w:style>";
  }

  var BLAUW = '<w:color w:val="1F4E79"/>';
  var KADER = '<w:pBdr><w:left w:val="single" w:sz="18" w:space="6" w:color="B9770E"/></w:pBdr>' +
    '<w:shd w:val="clear" w:color="auto" w:fill="FDF6E3"/>';
  var STYLES = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles ' + NS + ">" +
    '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" ' +
    'w:cs="Calibri"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="nl-NL"/></w:rPr></w:rPrDefault>' +
    '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>' +
    stijl("Normal", "Normal", "", "", "") +
    stijl("Title", "Title", '<w:spacing w:after="240"/><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="4" ' +
      'w:color="1F4E79"/></w:pBdr>', "<w:b/>" + BLAUW + '<w:sz w:val="40"/>') +
    stijl("Heading1", "heading 1", '<w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/>',
      "<w:b/>" + BLAUW + '<w:sz w:val="28"/>') +
    stijl("Heading2", "heading 2", '<w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="1"/>',
      '<w:b/><w:sz w:val="24"/>') +
    stijl("Heading3", "heading 3", '<w:keepNext/><w:spacing w:before="200" w:after="60"/><w:outlineLvl w:val="2"/>',
      "<w:b/>") +
    stijl("Lijst", "Lijst", '<w:tabs><w:tab w:val="left" w:pos="425"/></w:tabs><w:spacing w:after="60"/>' +
      '<w:ind w:left="425" w:hanging="425"/>') +
    stijl("Kader", "Kader", KADER + '<w:ind w:left="170" w:right="170"/>') +
    stijl("Kaderlijst", "Kaderlijst", KADER + '<w:tabs><w:tab w:val="left" w:pos="595"/></w:tabs>' +
      '<w:spacing w:after="60"/><w:ind w:left="595" w:right="170" w:hanging="425"/>') +
    stijl("Tabeltekst", "Tabeltekst", '<w:spacing w:after="0" w:line="240" w:lineRule="auto"/>', '<w:sz w:val="18"/>') +
    stijl("Tabeleinde", "Tabeleinde", '<w:spacing w:after="0" w:line="120" w:lineRule="exact"/>') +
    '<w:style w:type="table" w:styleId="Tabel"><w:name w:val="Tabel"/><w:tblPr><w:tblBorders>' +
    ["top", "left", "bottom", "right", "insideH", "insideV"].map(function (k) {
      return "<w:" + k + ' w:val="single" w:sz="4" w:space="0" w:color="C9D1DC"/>';
    }).join("") +
    '</w:tblBorders><w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>' +
    '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>' +
    "</w:styles>";
  var CONTENT_TYPES = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">' +
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>' +
    '<Default Extension="xml" ContentType="application/xml"/>' +
    '<Override PartName="/word/document.xml" ' +
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>' +
    '<Override PartName="/word/styles.xml" ' +
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>';
  var RELS = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" ' +
    'Target="word/document.xml"/></Relationships>';
  var DOC_RELS = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" ' +
    'Target="styles.xml"/></Relationships>';

  function delen(stukken) {
    return [["[Content_Types].xml", CONTENT_TYPES], ["_rels/.rels", RELS], ["word/document.xml", documentXml(stukken)],
            ["word/_rels/document.xml.rels", DOC_RELS], ["word/styles.xml", STYLES]];
  }

  // Een zip zonder compressie: genoeg voor Word, en zonder bibliotheek.
  var CRC = (function () {
    var t = [];
    for (var n = 0; n < 256; n++) {
      var c = n;
      for (var k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1;
      t.push(c >>> 0);
    }
    return t;
  })();
  function crc32(b) {
    var c = 0xFFFFFFFF;
    for (var i = 0; i < b.length; i++) c = CRC[(c ^ b[i]) & 0xFF] ^ (c >>> 8);
    return (c ^ 0xFFFFFFFF) >>> 0;
  }
  function utf8(s) { return new TextEncoder().encode(s); }

  function zip(bestanden) {
    var lokaal = [], centraal = [], plek = 0;
    function getal(n, lengte) { var a = []; for (var i = 0; i < lengte; i++) a.push((n >>> (8 * i)) & 0xFF); return a; }
    bestanden.forEach(function (f) {
      var naam = utf8(f[0]), data = utf8(f[1]), crc = crc32(data);
      // versie 20, geen vlaggen, opgeslagen, datum 1-1-1980
      var kop = [].concat(getal(0x04034b50, 4), getal(20, 2), getal(0, 2), getal(0, 2), getal(0, 2), getal(0x21, 2),
        getal(crc, 4), getal(data.length, 4), getal(data.length, 4), getal(naam.length, 2), getal(0, 2));
      lokaal.push(new Uint8Array(kop), naam, data);
      centraal.push(new Uint8Array([].concat(getal(0x02014b50, 4), getal(20, 2), getal(20, 2), getal(0, 2), getal(0, 2),
        getal(0, 2), getal(0x21, 2), getal(crc, 4), getal(data.length, 4), getal(data.length, 4), getal(naam.length, 2),
        getal(0, 2), getal(0, 2), getal(0, 2), getal(0, 2), getal(0, 4), getal(plek, 4))), naam);
      plek += kop.length + naam.length + data.length;
    });
    var grootte = centraal.reduce(function (s, x) { return s + x.length; }, 0);
    var eind = new Uint8Array([].concat(getal(0x06054b50, 4), getal(0, 2), getal(0, 2), getal(bestanden.length, 2),
      getal(bestanden.length, 2), getal(grootte, 4), getal(plek, 4), getal(0, 2)));
    var delen = lokaal.concat(centraal, [eind]);
    var uit = new Uint8Array(delen.reduce(function (s, x) { return s + x.length; }, 0)), p = 0;
    delen.forEach(function (x) { uit.set(x, p); p += x.length; });
    return uit;
  }

  function docx(stukken) { return zip(delen(stukken)); }

  var api = { documentXml: documentXml, delen: delen, docx: docx, crc32: crc32 };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else wereld.BeleidssetWord = api;
})(this);
