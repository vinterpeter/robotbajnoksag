"""Robotgyár: önálló HTML-oldal, ami véletlen adatokból rak össze robotot a rajzlap alkatrészeiből.
Az alkatrészek a general.py-ból jönnek (ugyanazok, mint a nyomtatható lapon), itt bővülnek és kapnak illesztési pontot."""
import json, re
import general as g
from general import r, c, e, p, pg, pl

def lista(adat, sor): return dict(next(v for n, v in adat if n == sor))
FEJ, SZEM, SZAJ, KAR, LAB, KELLEK = (lista(g.ALKATRESZEK, n) for n in ('Fej', 'Szem', 'Száj', 'Kar', 'Láb', 'Kellék'))
FEGYVER, RAKETA, PILOTA, REPULES = (lista(g.FELSZERELES, n) for n in ('Fegyver', 'Rakéta', 'Pilóta helye', 'Repülés'))

# ---- új alkatrészek ----
TEST = {'doboz': [r(8, 8, 44, 44, 3)], 'hordó': [p('M12,8 H48 Q57,30 48,52 H12 Q3,30 12,8 Z')], 'széles vállú': [pg('5,8 55,8 44,52 16,52')], 'gömb': [c(30, 30, 23)],
        'harang': [pg('16,8 44,8 55,52 5,52')], 'páncél': [pg('9,8 51,8 57,30 44,52 16,52 3,30')], 'tévé': [r(5, 10, 50, 40, 9)], 'tojás': [e(30, 30, 20, 23)]}
FEJ.update({'tévé': [r(8, 14, 44, 34, 8)], 'háromszög': [pg('30,10 52,48 8,48')], 'lapos': [r(6, 20, 48, 24, 6)]})
SZEM.update({'mérges': [c(19, 32, 8), c(41, 32, 8), c(20, 33, 3), c(40, 33, 3), p('M9,20 L27,26 M51,20 L33,26')], 'álmos': [p('M10,30 Q19,38 28,30 M32,30 Q41,38 50,30'), p('M10,30 L28,30 M32,30 L50,30')]})
SZAJ.update({'ámuló': [e(30, 30, 9, 12)], 'bajuszos': [p('M10,26 Q20,16 30,26 Q40,16 50,26'), p('M18,38 L42,39')]})
KAR.update({'csáp': [p('M6,30 Q16,12 26,30 T46,30'), c(50, 30, 4)], 'fúró': [r(6, 22, 22, 16), pg('28,18 54,30 28,42'), p('M34,21 L36,39 M41,24 L43,36')]})
LAB.update({'gólyaláb': [p('M30,8 V50'), p('M21,50 L39,51')], 'lépegető': [pl('30,8 20,24 34,38 30,50'), p('M22,50 L41,51')]})
KELLEK.update({'korona': [pg('10,46 10,22 20,34 30,16 40,34 50,22 50,46')], 'szív': [p('M30,48 Q6,30 14,18 Q24,10 30,22 Q36,10 46,18 Q54,30 30,48 Z')]})
del KELLEK['rakétahát']
FEGYVER.update({'lángszóró': [r(8, 24, 26, 14, 3), r(34, 27, 10, 8), pl('44,24 56,26 48,31 58,34 44,38')], 'szigony': [p('M30,54 V16'), p('M18,22 V10 M42,22 V10 M18,22 Q30,32 42,22 M30,16 V8')]})
REPULES['szárny'] = [pg('24,22 2,36 24,40'), pg('36,22 58,36 36,40')]
REPULES['denevérszárny'] = [p('M26,20 L3,13 L8,26 L3,35 L12,33 L14,43 L26,37 Z'), p('M34,20 L57,13 L52,26 L57,35 L48,33 L46,43 L34,37 Z')]

def fajta(el):
    """k = zárt, kitölthető; a = apró (pupilla, gomb); n = nyitott vonal"""
    m = re.search(r'<circle[^>]* r="([\d.]+)"', el)
    if m: return 'a' if float(m.group(1)) <= 3.5 else 'k'
    m = re.search(r'<rect[^>]* width="([\d.]+)" height="([\d.]+)"', el)
    if m: return 'a' if max(float(m.group(1)), float(m.group(2))) <= 6 else 'k'
    if el.startswith(('<ellipse', '<polygon')): return 'k'
    return 'k' if el.startswith('<path') and re.search(r'Z"/>$', el) else 'n'

def csomag(szotar, **kozos):
    """kozos: illesztés alapértéke; egyedi felülírás az EGYEDI szótárból jön"""
    return [dict(nev=n, el=[[x, fajta(x)] for x in els], **{**kozos, **EGYEDI.get(n, {})}) for n, els in szotar.items()]

# illesztési pont (ax, ay) az alkatrész saját 60x60-as rajzán; hely = hová kerül a roboton
EGYEDI = {
    'fogó': dict(ax=8, ay=20), 'rugó': dict(ax=6, ay=30), 'könyökös': dict(ax=8, ay=14), 'ágyú': dict(ax=6, ay=30), 'kard': dict(ax=8, ay=50), 'kalapács': dict(ax=8, ay=48),
    'csáp': dict(ax=6, ay=30), 'fúró': dict(ax=6, ay=30),
    'oszlop': dict(ax=29, ay=8), 'kerék': dict(ax=30, ay=8), 'lánctalp': dict(ax=30, ay=10, egy=1, s=2.3), 'rugóláb': dict(ax=30, ay=8), 'pókláb': dict(ax=30, ay=10, egy=1, s=2.5),
    'gólyaláb': dict(ax=30, ay=8), 'lépegető': dict(ax=30, ay=8),
    'antenna': dict(hely='fejteto', ax=30, ay=52, mag=44), 'korona': dict(hely='fejteto', ax=30, ay=46, mag=30),
    'üvegkupola': dict(hely='fejteto', ax=30, ay=46, mag=36), 'nyitott ülés': dict(hely='fejteto', ax=30, ay=46, mag=36), 'kabin létrával': dict(hely='fejteto', ax=36, ay=33, mag=28),
    'távirányító': dict(hely='kulso'), 'kormány': dict(hely='mell', s=0.8),
    'propeller': dict(hely='fejteto', ax=30, ay=54, mag=30, s=1.2), 'sugárhajtómű': dict(hely='oldal'), 'léggömb': dict(hely='folott', ax=30, ay=57), 'ejtőernyő': dict(hely='folott', ax=30, ay=58),
    'csészealj': dict(hely='alatt'), 'szárny': dict(hely='hat'), 'denevérszárny': dict(hely='hat'),
}
ADAT = dict(
    test=csomag(TEST), fej=csomag(FEJ), szem=csomag(SZEM), szaj=csomag(SZAJ), kar=csomag(KAR, ax=6, ay=30), lab=csomag(LAB, ax=30, ay=8),
    kellek=csomag(KELLEK, hely='mell'), fegyver=csomag(FEGYVER, ax=30, ay=54), raketa=csomag(RAKETA, ax=30, ay=54), pilota=csomag(PILOTA, hely='mell'), repules=csomag(REPULES, hely='hat'))

SABLON = open('robotgyar_sablon.html').read()
open('robotgyar.html', 'w').write(SABLON.replace('/*ADAT*/', 'const ADAT = ' + json.dumps(ADAT, ensure_ascii=False) + ';'))
print({k: len(v) for k, v in ADAT.items()})

# a játék ugyanazt az alkatrészkészletet kapja
JATEK = open('robotjatek_sablon.html').read()
_jatek = JATEK.replace('/*ADAT*/', 'const ADAT = ' + json.dumps(ADAT, ensure_ascii=False) + ';')
for _f in ('robotbajnoksag.html', 'index.html'):   # az index.html ugyanaz a játék, hogy a repó gyökeréből is induljon
    open(_f, 'w').write(_jatek)
