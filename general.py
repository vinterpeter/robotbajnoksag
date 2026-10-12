"""Robotrajzoló lap (A4, 2 oldal): kockadobós alkatrész-készlet + öt robot lépésről lépésre."""
SOTET, UJ = '#3a3a3a', '#e2452b'

def r(x, y, w, h, rx=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'
def c(x, y, rr): return f'<circle cx="{x}" cy="{y}" r="{rr}"/>'
def e(x, y, a, b): return f'<ellipse cx="{x}" cy="{y}" rx="{a}" ry="{b}"/>'
def p(d): return f'<path d="{d}"/>'
def pg(pts): return f'<polygon points="{pts}"/>'
def pl(pts): return f'<polyline points="{pts}"/>'

# ---------- 1. oldal: kockadobós alkatrészek (60x60-as rajzok) ----------
ALKATRESZEK = [
 ('Fej', [('kocka', [r(12, 12, 36, 36)]), ('gömb', [c(30, 30, 19)]), ('vödör', [pg('14,12 46,12 52,48 8,48')]), ('tölcsér', [pg('8,14 52,14 38,48 22,48')]),
          ('kupola', [p('M10,48 V30 A20,20 0 0 1 50,30 V48 Z')]), ('hatszög', [pg('20,12 40,12 52,30 40,48 20,48 8,30')])]),
 ('Szem', [('két kör', [c(19, 30, 9), c(41, 30, 9), c(21, 31, 3), c(43, 31, 3)]), ('két kocka', [r(11, 22, 16, 16), r(33, 22, 16, 16), r(17, 28, 5, 5), r(39, 28, 5, 5)]),
           ('küklopsz', [c(30, 30, 16), c(30, 30, 7), c(32, 28, 2)]), ('napszemüveg', [r(8, 22, 44, 14, 7), c(40, 29, 3)]),
           ('lézerszem', [p('M12,22 L24,34 M24,22 L12,34'), c(42, 28, 8), c(42, 28, 2)]), ('három szem', [c(14, 32, 6), c(30, 26, 6), c(46, 32, 6)])]),
 ('Száj', [('rács', [r(12, 20, 36, 20), p('M21,20 V40 M30,20 V40 M39,20 V40')]), ('cikkcakk', [pl('8,34 15,24 22,34 29,24 36,34 43,24 50,34')]), ('vonal', [p('M12,30 Q30,33 48,29')]),
           ('mosoly', [p('M12,24 Q30,46 48,24')]), ('hangszóró', [c(30, 30, 17), c(24, 25, 2), c(36, 25, 2), c(30, 31, 2), c(24, 37, 2), c(36, 37, 2)]),
           ('fogas', [r(10, 20, 40, 20), pl('10,20 15,30 20,20 25,30 30,20 35,30 40,20 45,30 50,20')])]),
 ('Kar', [('fogó', [p('M8,20 H38'), p('M52,10 A10,10 0 1 0 52,30')]), ('rugó', [pl('6,30 12,18 18,42 24,18 30,42 36,18 42,42 46,30'), c(51, 30, 5)]),
          ('könyökös', [p('M8,14 H30 V44'), c(30, 14, 4), r(24, 44, 12, 9)]), ('ágyú', [r(6, 22, 30, 16), r(36, 17, 16, 26), c(44, 30, 5)]),
          ('kard', [p('M8,50 L18,40'), p('M12,34 L24,46'), p('M18,40 L50,8')]), ('kalapács', [p('M8,48 L36,20'), pg('28,12 46,30 52,24 34,6')])]),
 ('Láb', [('oszlop', [r(22, 8, 14, 34), r(14, 42, 30, 10)]), ('kerék', [r(26, 8, 8, 18), c(30, 38, 14), c(30, 38, 4)]), ('lánctalp', [r(6, 28, 48, 20, 10), c(16, 38, 5), c(30, 38, 5), c(44, 38, 5), r(24, 10, 12, 18)]),
          ('rugóláb', [pl('30,8 18,14 42,20 18,26 42,32 30,38'), e(30, 44, 16, 6)]), ('rakéta', [pg('20,8 40,8 44,32 16,32'), pl('18,34 22,48 26,36 30,52 34,36 38,48 42,34')]),
          ('pókláb', [p('M30,10 L10,26 L8,50'), p('M30,10 L30,50'), p('M30,10 L50,26 L52,50'), c(30, 10, 4)])]),
 ('Kellék', [('antenna', [p('M30,52 V18'), c(30, 12, 6), p('M16,10 Q10,16 16,22 M44,10 Q50,16 44,22')]), ('gombok', [r(8, 14, 44, 32, 4), c(19, 26, 5), c(30, 26, 5), c(41, 26, 5), p('M14,38 H46')]),
             ('fogaskerék', [c(30, 30, 13), c(30, 30, 5), p('M30,10 V17 M30,43 V50 M10,30 H17 M43,30 H50 M16,16 L21,21 M39,39 L44,44 M44,16 L39,21 M16,44 L21,39')]),
             ('mérőóra', [c(30, 30, 18), p('M30,30 L42,20'), p('M16,30 H20 M40,30 H44 M30,16 V20')]), ('elem', [r(8, 18, 40, 24, 3), r(48, 25, 5, 10), p('M17,30 H25 M21,26 V34 M33,30 H41')]),
             ('rakétahát', [r(12, 10, 14, 28, 6), r(34, 10, 14, 28, 6), pl('13,40 16,52 19,42 22,52 25,40'), pl('35,40 38,52 41,42 44,52 47,40')])]),
]

# ---------- 2. oldal: öt robot három lépésben (120x140-es rajzok) ----------
# mindegyik: név, [1. lépés, 2. lépés, 3. lépés], [(kitöltendő alakzat, szín)]
ROBOTOK = [
 ('Dobozrobot',
  [[r(40, 18, 40, 32), r(32, 54, 56, 46)],
   [c(52, 32, 5), c(68, 32, 5), p('M50,43 H70'), p('M60,18 V9'), c(60, 6, 3), c(48, 70, 4), c(60, 70, 4), c(72, 70, 4)],
   [p('M32,62 H18 V84'), p('M88,62 H102 V84'), p('M13,84 a5,5 0 0 0 10,0'), p('M97,84 a5,5 0 0 0 10,0'), r(42, 100, 10, 22), r(68, 100, 10, 22), r(36, 122, 22, 8), r(62, 122, 22, 8)]],
  [(r(40, 18, 40, 32), '#8fc4ee'), (r(32, 54, 56, 46), '#f5b95c'), (r(36, 122, 22, 8), '#9a9a9a'), (r(62, 122, 22, 8), '#9a9a9a'), (c(48, 70, 4), '#e2452b'), (c(60, 70, 4), '#f2d43a'), (c(72, 70, 4), '#5cb85c')]),
 ('Guruló robot',
  [[p('M38,50 A22,22 0 0 1 82,50 Z'), pg('34,54 86,54 96,104 24,104')],
   [r(46, 35, 28, 9, 4), c(66, 39.5, 2.5), c(40, 116, 12), c(80, 116, 12), c(40, 116, 3), c(80, 116, 3), c(60, 80, 11), p('M60,80 L67,73')],
   [pl('31,64 20,68 28,75 17,81 25,88'), pl('89,64 100,68 92,75 103,81 95,88'), p('M19,90 a6,6 0 0 0 12,0'), p('M89,90 a6,6 0 0 0 12,0'), p('M50,30 L44,15'), p('M70,30 L76,15'), c(43, 12, 3), c(77, 12, 3)]],
  [(p('M38,50 A22,22 0 0 1 82,50 Z'), '#b6e3a1'), (pg('34,54 86,54 96,104 24,104'), '#ef8f6b'), (c(40, 116, 12), '#777'), (c(80, 116, 12), '#777'), (c(60, 80, 11), '#fff3b0')]),
 ('Rugós gömbrobot',
  [[c(60, 30, 18), c(60, 76, 25)],
   [c(60, 29, 8), c(61, 28, 3), pl('51,41 55,38 59,41 63,38 67,41'), r(37, 24, 5, 12), r(78, 24, 5, 12), r(50, 68, 20, 14, 2), p('M54,75 H66')],
   [pl('50,100 42,105 56,110 42,115 56,120 48,125'), pl('70,100 62,105 76,110 62,115 76,120 68,125'), e(47, 129, 11, 4), e(69, 129, 11, 4), p('M37,68 L20,56'), p('M83,68 L100,56'), c(17, 54, 5), c(103, 54, 5), pl('60,12 56,8 64,5 60,1')]],
  [(c(60, 30, 18), '#f2d43a'), (c(60, 76, 25), '#c79be8'), (c(17, 54, 5), '#e2452b'), (c(103, 54, 5), '#e2452b'), (r(50, 68, 20, 14, 2), '#ffffff')]),
 ('Harci óriásrobot',
  [[r(34, 36, 52, 48), r(50, 18, 20, 16)],
   [r(15, 34, 19, 15), r(86, 34, 19, 15), p('M53,26 H67'), pg('47,46 73,46 60,68'), r(19, 22, 9, 12), r(92, 22, 9, 12)],
   [r(17, 49, 14, 32), r(89, 49, 14, 32), c(24, 88, 8), c(96, 88, 8), r(40, 84, 16, 36), r(64, 84, 16, 36), pg('34,130 38,120 58,120 58,130'), pg('62,130 62,120 82,120 86,130')]],
  [(r(34, 36, 52, 48), '#e2655a'), (r(50, 18, 20, 16), '#bdbdbd'), (r(15, 34, 19, 15), '#5b8fd6'), (r(86, 34, 19, 15), '#5b8fd6'), (pg('47,46 73,46 60,68'), '#f2d43a'), (c(24, 88, 8), '#777'), (c(96, 88, 8), '#777')]),
 ('Robotkutya',
  [[r(26, 62, 60, 30, 3), r(76, 36, 30, 26, 3)],
   [c(95, 47, 4), r(106, 48, 9, 8), pg('79,36 84,21 91,36'), p('M92,56 H104'), p('M28,66 L14,48'), c(12, 45, 3.5), c(42, 77, 4), c(56, 77, 4), c(70, 77, 4)],
   [r(31, 92, 8, 24), r(45, 92, 8, 24), r(64, 92, 8, 24), r(77, 92, 8, 24), r(28, 116, 14, 6), r(42, 116, 14, 6), r(61, 116, 14, 6), r(74, 116, 14, 6), p('M76,60 H86')]],
  [(r(26, 62, 60, 30, 3), '#9ad1c9'), (r(76, 36, 30, 26, 3), '#9ad1c9'), (pg('79,36 84,21 91,36'), '#e2452b'), (r(106, 48, 9, 8), '#555'), (c(12, 45, 3.5), '#f2d43a')]),
]

# ---------- 3. oldal: harci felszerelés és pilótafülke (kockadobós, 60x60) ----------
FELSZERELES = [
 ('Fegyver', [('lézerkard', [r(27, 6, 6, 34, 3), p('M20,40 L40,41'), r(26, 41, 8, 14)]),
              ('pajzs', [p('M12,10 H48 V30 Q48,46 30,54 Q12,46 12,30 Z'), p('M30,10 V54 M12,28 H48')]),
              ('lézerpisztoly', [pg('8,20 40,20 40,30 22,30 20,46 10,46 12,30 8,30'), r(40, 22, 10, 6), c(53, 25, 3)]),
              ('buzogány', [p('M8,52 L24,36'), c(28, 32, 2), c(33, 27, 2), c(43, 17, 9), p('M43,4 V8 M43,26 V30 M30,17 H34 M52,17 H56 M34,8 L37,11 M52,26 L49,23 M52,8 L49,11 M34,26 L37,23')]),
              ('villámvető', [r(6, 22, 24, 16, 3), pl('30,30 40,18 40,30 54,16'), pl('30,34 42,42 40,34 54,44')]),
              ('mágnes', [p('M16,12 V34 A14,14 0 0 0 44,34 V12 H36 V34 A6,6 0 0 1 24,34 V12 Z'), p('M16,20 L24,21 M36,20 L44,21')])]),
 ('Rakéta', [('rakéta', [p('M30,6 Q40,18 40,34 H20 Q20,18 30,6 Z'), pg('20,26 12,38 20,36'), pg('40,26 48,38 40,36'), c(30, 22, 4), pl('22,36 25,48 30,40 35,50 38,36')]),
             ('rakétavető', [r(8, 12, 44, 36, 4), c(20, 23, 6), c(40, 23, 6), c(20, 38, 6), c(40, 38, 6)]),
             ('bomba', [c(28, 36, 16), r(24, 15, 8, 6), p('M28,15 Q30,6 40,8'), p('M43,3 L45,7 M48,8 L44,9 M46,13 L43,11')]),
             ('torpedó', [p('M8,30 Q8,22 16,22 H40 Q54,30 40,38 H16 Q8,38 8,30 Z'), p('M12,22 L5,15 M12,38 L5,45'), c(36, 30, 3.5), p('M22,22 V38')]),
             ('tűzgolyó', [c(40, 30, 11), pl('32,22 8,18 22,26 4,30 22,34 8,42 32,38'), c(40, 30, 4)]),
             ('lézersugár', [r(4, 23, 14, 14, 2), p('M18,27 L48,26 M18,33 L48,34'), p('M48,20 L55,13 M50,30 L58,30 M48,40 L55,47')])]),
 ('Pilóta helye', [('üvegkupola', [p('M10,46 V30 A20,20 0 0 1 50,30 V46 Z'), c(30, 30, 6), p('M19,46 Q30,34 41,46')]),
                   ('ablak a hasán', [r(8, 8, 44, 44, 4), r(17, 17, 26, 20, 3), c(30, 26, 5), p('M21,37 Q30,29 39,37')]),
                   ('nyitott ülés', [p('M14,14 V46 H48'), c(27, 18, 6), p('M27,24 V40 H40'), p('M27,30 L41,27'), p('M44,46 L47,25'), c(47, 22, 3)]),
                   ('kabin létrával', [r(20, 6, 32, 26, 4), c(36, 18, 5), p('M28,27 Q36,21 44,27'), p('M6,32 L54,33'), p('M10,33 V56 M19,33 V56 M10,40 L19,40 M10,47 L19,47 M10,54 L19,54')]),
                   ('kormány', [c(30, 26, 15), c(30, 26, 4), p('M30,11 V22 M17,34 L26,28 M43,34 L34,28'), p('M30,41 V55')]),
                   ('távirányító', [r(12, 24, 34, 26, 5), p('M40,24 L46,9'), c(46, 6, 2.5), c(23, 37, 5), c(37, 32, 2.5), c(37, 42, 2.5), p('M51,13 Q57,9 54,3')])]),
 ('Repülés', [('szárny', [r(24, 12, 12, 34, 5), pg('24,22 4,36 24,38'), pg('36,22 56,36 36,38')]),
              ('propeller', [p('M30,30 V54'), c(30, 26, 4), e(15, 26, 11, 4), e(45, 26, 11, 4)]),
              ('sugárhajtómű', [r(12, 20, 32, 20, 4), pg('44,20 54,26 54,34 44,40'), pl('12,22 3,26 9,30 1,32 9,35 4,39 12,38')]),
              ('léggömb', [c(30, 22, 16), p('M24,37 L26,48 M36,37 L34,48'), r(24, 48, 12, 8)]),
              ('ejtőernyő', [p('M8,28 A22,20 0 0 1 52,28 Z'), p('M8,28 L27,50 M52,28 L33,50 M30,28 V50'), r(25, 50, 10, 7)]),
              ('csészealj', [e(30, 36, 24, 8), p('M18,31 A12,12 0 0 1 42,31'), c(18, 37, 2), c(30, 39, 2), c(42, 37, 2), p('M22,46 L18,54 M38,46 L42,54')])]),
]

# ---------- 4. oldal: pilóta és négy harci gép lépésről lépésre (120x136) ----------
_LANG = '46,108 50,124 55,112 60,132 65,112 70,124 74,108'
GEPEK = [
 ('Pilóta az ülésben',
  [[c(60, 36, 14), r(44, 52, 32, 38, 8), p('M34,44 V98 H96')],
   [c(55, 37, 1.8), c(65, 37, 1.8), p('M54,42 Q60,47 66,42'), p('M45,33 A15,15 0 0 1 75,33 Z'), p('M47,60 L73,84')],
   [p('M46,64 L28,80'), p('M74,64 L92,80'), p('M26,104 L28,78'), p('M94,104 L92,78'), c(28, 76, 4), c(92, 76, 4), r(22, 104, 76, 16, 3), c(40, 112, 3), c(52, 112, 3), r(64, 108, 24, 8)]],
  [(p('M45,33 A15,15 0 0 1 75,33 Z'), '#e2452b'), (r(44, 52, 32, 38, 8), '#5b8fd6'), (r(22, 104, 76, 16, 3), '#bdbdbd'), (c(40, 112, 3), '#e2452b'), (c(52, 112, 3), '#5cb85c'), (c(28, 76, 4), '#f2d43a'), (c(92, 76, 4), '#f2d43a')]),
 ('Pilótás óriásrobot',
  [[p('M42,40 A18,18 0 0 1 78,40 Z'), r(30, 40, 60, 44)],
   [c(60, 31, 5.5), p('M51,40 Q60,33 69,40'), c(46, 53, 4), c(60, 53, 4), c(74, 53, 4), r(44, 64, 32, 12), p('M52,64 V76 M60,64 V76 M68,64 V76'), r(11, 33, 19, 14), r(90, 33, 19, 14), c(20.5, 40, 3.5), c(99.5, 40, 3.5)],
   [r(14, 47, 13, 31), r(93, 47, 13, 31), p('M14,80 a6.5,6.5 0 0 0 13,0'), p('M93,80 a6.5,6.5 0 0 0 13,0'), r(38, 84, 16, 32), r(66, 84, 16, 32), pg('30,128 36,116 56,116 56,128'), pg('64,128 64,116 84,116 90,128')]],
  [(p('M42,40 A18,18 0 0 1 78,40 Z'), '#bfe3f7'), (r(30, 40, 60, 44), '#7cc47a'), (r(11, 33, 19, 14), '#f29a4a'), (r(90, 33, 19, 14), '#f29a4a'), (pg('30,128 36,116 56,116 56,128'), '#9a9a9a'), (pg('64,128 64,116 84,116 90,128'), '#9a9a9a'),
   (c(46, 53, 4), '#e2452b'), (c(60, 53, 4), '#f2d43a'), (c(74, 53, 4), '#e2452b')]),
 ('Rakétarobot',
  [[p('M60,10 Q80,30 80,62 V92 H40 V62 Q40,30 60,10 Z')],
   [r(48, 36, 24, 10, 5), c(66, 41, 2.5), p('M40,64 L80,65'), pg('40,68 24,96 40,92'), pg('80,68 96,96 80,92'), c(60, 78, 6)],
   [p('M42,54 L22,44'), p('M78,54 L98,44'), c(19, 42, 5), c(101, 42, 5), pl('42,94 46,114 52,100 60,126 68,100 74,114 78,94'), p('M12,66 V88 M108,66 V88 M18,100 V116 M102,100 V116')]],
  [(p('M60,10 Q80,30 80,62 V92 H40 V62 Q40,30 60,10 Z'), '#e2655a'), (pg('40,68 24,96 40,92'), '#5b8fd6'), (pg('80,68 96,96 80,92'), '#5b8fd6'), (pg('42,94 46,114 52,100 60,126 68,100 74,114 78,94'), '#f29a4a'),
   (r(48, 36, 24, 10, 5), '#fff3b0'), (c(60, 78, 6), '#f2d43a')]),
 ('Ágyús lánctalpas',
  [[r(16, 92, 84, 30, 15), pg('28,92 34,56 82,56 88,92')],
   [c(32, 107, 8), c(49, 107, 8), c(67, 107, 8), c(84, 107, 8), p('M46,56 A12,12 0 0 1 70,56 Z'), c(58, 50, 4.5), c(40, 76, 5)],
   [r(86, 66, 22, 8), r(108, 63, 6, 14), r(18, 40, 22, 15), c(25, 47.5, 3.5), c(34, 47.5, 3.5), p('M22,55 L30,62'), p('M76,56 L82,36'), c(83, 33, 3)]],
  [(pg('28,92 34,56 82,56 88,92'), '#9bb86a'), (r(16, 92, 84, 30, 15), '#9a9a9a'), (p('M46,56 A12,12 0 0 1 70,56 Z'), '#bfe3f7'), (r(18, 40, 22, 15), '#e2655a'), (c(40, 76, 5), '#f2d43a'), (r(86, 66, 22, 8), '#777')]),
 ('Űrrakéta pilótával',
  [[p('M60,8 Q84,34 84,70 V98 H36 V70 Q36,34 60,8 Z')],
   [c(60, 50, 13), c(60, 48, 5), p('M51,58 Q60,50 69,58'), p('M36,76 L84,77'), p('M46,27 Q60,34 74,27')],
   [pg('36,72 16,104 36,98'), pg('84,72 104,104 84,98'), r(46, 98, 28, 8), pl(_LANG), p('M14,20 L18,24 M18,20 L14,24 M100,34 L104,38 M104,34 L100,38')]],
  [(p('M60,8 Q84,34 84,70 V98 H36 V70 Q36,34 60,8 Z'), '#e8e8e8'), (p('M60,8 Q74,22 74,27 Q60,34 46,27 Q46,22 60,8 Z'), '#e2452b'), (c(60, 50, 13), '#bfe3f7'), (pg('36,72 16,104 36,98'), '#e2452b'), (pg('84,72 104,104 84,98'), '#e2452b'),
   (pg(_LANG), '#f29a4a')]),
]

def rajz(elemek, szin, vast): return f'<g fill="none" stroke="{szin}" stroke-width="{vast}" stroke-linecap="round" stroke-linejoin="round" filter="url(#kez)">{"".join(elemek)}</g>'
def festek(lista): return ''.join(f'<g fill="{sz}" fill-opacity="0.62" stroke="none" filter="url(#kez)">{al}</g>' for al, sz in lista)

SZURO = """<svg width="0" height="0" style="position:absolute"><defs>
<filter id="kez" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4" result="z"/><feDisplacementMap in="SourceGraphic" in2="z" scale="2.6"/></filter>
</defs></svg>"""

POTTY = {1: [(30, 30)], 2: [(18, 18), (42, 42)], 3: [(16, 16), (30, 30), (44, 44)], 4: [(18, 18), (42, 18), (18, 42), (42, 42)],
         5: [(16, 16), (44, 16), (30, 30), (16, 44), (44, 44)], 6: [(18, 15), (42, 15), (18, 30), (42, 30), (18, 45), (42, 45)]}
KOCKAK = ''.join('<th><svg viewBox="0 0 60 60" class="kocka"><rect x="6" y="6" width="48" height="48" rx="9" fill="#fff" stroke="#3a3a3a" stroke-width="3"/>'
                 + ''.join(f'<circle cx="{x}" cy="{y}" r="4.6" fill="#3a3a3a"/>' for x, y in POTTY[n]) + '</svg></th>' for n in range(1, 7))
LEPESEK = ['1. Nagy formák', '2. Arc és részletek', '3. Karok és lábak', '4. Színezd ki!']
LEPESEK2 = ['1. Nagy formák', '2. Pilóta és részletek', '3. Fegyver és hajtómű', '4. Színezd ki!']

def keszlet(adat):
    sorok = ''
    for nev, valtozatok in adat:
        cellak = ''.join(f'<td><svg viewBox="0 0 60 60">{rajz(el, SOTET, 2.2)}</svg><span>{cim}</span></td>' for cim, el in valtozatok)
        sorok += f'<tr><th>{nev}</th>{cellak}</tr>'
    return f'<table class="keszlet"><colgroup><col style="width:21mm"><col><col><col><col><col><col></colgroup><thead><tr><th></th>{KOCKAK}</tr></thead><tbody>{sorok}</tbody></table>'

def lepesek(adat, fejlec):
    sorok = ''
    for nev, lep, szinek in adat:
        cellak = ''
        for k in range(4):
            if k < 3: belso = rajz(sum(lep[:k], []), SOTET, 2.2) + rajz(lep[k], UJ, 2.8)
            else: belso = festek(szinek) + rajz(sum(lep, []), SOTET, 2.2)
            cellak += f'<td><svg viewBox="0 0 120 136">{belso}</svg></td>'
        sorok += f'<tr><th><span>{nev}</span></th>{cellak}</tr>'
    return f'<table class="lepesek"><colgroup><col style="width:13mm"><col><col><col><col></colgroup><thead><tr><th></th>{"".join(f"<th>{l}</th>" for l in fejlec)}</tr></thead><tbody>{sorok}</tbody></table>'

def lab(n): return f'<div class="lab"><span>Rajzoljunk robotot!</span><span>{n}&nbsp;/&nbsp;4</span></div>'

html = f"""<!doctype html><html lang="hu"><head><meta charset="utf-8"><title>Rajzoljunk robotot!</title><style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
html {{ hyphens: none; }}
body {{ margin: 0; font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif; color: #2e2e2e; }}
.lap {{ width: 210mm; height: 297mm; padding: 12mm 13mm 14mm; position: relative; page-break-after: always; overflow: hidden; }}
.lap:last-child {{ page-break-after: auto; }}
h1 {{ font-family: "Chalkboard SE", "Marker Felt", "Avenir Next", sans-serif; font-size: 27pt; margin: 0 0 1.5mm; color: #e2452b; letter-spacing: .3pt; }}
.alcim {{ font-size: 11.5pt; margin: 0 0 5mm; color: #555; }}
h2 {{ font-family: "Chalkboard SE", "Marker Felt", "Avenir Next", sans-serif; font-size: 15pt; margin: 0 0 2mm; color: #2e2e2e; }}
.szabalyok {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; margin-bottom: 6mm; }}
.szabalyok.also {{ margin: 5mm 0 0; }}
.szabaly {{ border: 1.6pt solid #3a3a3a; border-radius: 4mm; padding: 3mm 3.5mm; font-size: 10.5pt; line-height: 1.38; background: #fff8e6; }}
.szabaly b {{ display: block; font-family: "Chalkboard SE", "Marker Felt", sans-serif; font-size: 12.5pt; color: #e2452b; margin-bottom: .8mm; }}
.leiras {{ font-size: 10.5pt; line-height: 1.4; margin: 0 0 3mm; }}
table {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
.keszlet th, .keszlet td {{ border: 1.1pt solid #9a9a9a; text-align: center; vertical-align: middle; padding: 1mm 0 1.2mm; }}
.keszlet thead th {{ border: none; padding-bottom: 1mm; }}
.keszlet tbody th {{ font-family: "Chalkboard SE", "Marker Felt", sans-serif; font-size: 13pt; background: #eef6ff; line-height: 1.15; }}
.keszlet td svg {{ width: 21.5mm; height: 21.5mm; display: block; margin: 0 auto; }}
.nagy .keszlet td svg {{ width: 22mm; height: 22mm; }}
.nagy .keszlet th, .nagy .keszlet td {{ padding: 1.2mm 0 1.5mm; }}
.keszlet td span {{ font-size: 8.8pt; color: #555; display: block; margin-top: -.5mm; white-space: nowrap; }}
.kocka {{ width: 10mm; height: 10mm; display: block; margin: 0 auto; }}
.lepesek th, .lepesek td {{ border: 1.1pt solid #9a9a9a; text-align: center; vertical-align: middle; padding: 0; }}
.lepesek thead th {{ border: none; font-size: 10.5pt; font-weight: 600; padding: 0 0 1.5mm; color: #444; white-space: nowrap; }}
.lepesek tbody th {{ background: #eef6ff; }}
.lepesek tbody th span {{ display: block; writing-mode: vertical-rl; transform: rotate(180deg); font-family: "Chalkboard SE", "Marker Felt", sans-serif; font-size: 12pt; margin: 0 auto; white-space: nowrap; }}
.lepesek td svg {{ width: 39mm; height: 44.2mm; display: block; margin: .8mm auto; }}
.terv {{ display: grid; grid-template-columns: 1.15fr 1fr; gap: 5mm; margin-top: 5mm; height: 66mm; }}
.rajzhely {{ border: 1.8pt dashed #3a3a3a; border-radius: 5mm; position: relative; }}
.rajzhely span {{ position: absolute; left: 4mm; top: 3mm; font-size: 9.5pt; color: #888; }}
.adatok {{ border: 1.6pt solid #3a3a3a; border-radius: 4mm; padding: 3.5mm 4.5mm; background: #eef6ff; }}
.adatok p {{ font-size: 10.5pt; margin: 0; height: 10mm; border-bottom: 1pt solid #8a8a8a; display: flex; align-items: flex-end; padding-bottom: 1mm; color: #444; }}
.jel {{ font-size: 10pt; color: #555; margin: 0 0 3.5mm; }}
.jel i {{ font-style: normal; color: #e2452b; font-weight: 700; }}
.lab {{ position: absolute; left: 13mm; right: 13mm; bottom: 6mm; font-size: 8.5pt; color: #888; display: flex; justify-content: space-between; }}
</style></head><body>{SZURO}
<section class="lap">
  <h1>Rajzoljunk robotot!</h1>
  <p class="alcim">Minden robot néhány egyszerű formából áll. Aki tud négyzetet és kört rajzolni, az robotot is tud.</p>
  <div class="szabalyok">
    <div class="szabaly"><b>1. Formákból építünk</b>Négyzet, téglalap, kör, háromszög. Előbb a&nbsp;nagy darabok: fej és test.</div>
    <div class="szabaly"><b>2. Utána a&nbsp;részletek</b>Szem, száj, antenna, gombok, végül a&nbsp;karok és a&nbsp;lábak.</div>
    <div class="szabaly"><b>3. Nincs elrontott robot</b>A ferde vonaltól lesz egyedi. Ami nem tetszik, abból lesz a&nbsp;páncél vagy a&nbsp;rozsda.</div>
  </div>
  <h2>Kockadobós robotgyár</h2>
  <p class="leiras">Dobj a&nbsp;kockával minden sorhoz egyszer! Amelyik számot dobtad, azt az alkatrészt rajzold le. Hat dobás után kész a&nbsp;robotod, amilyet még senki sem látott. Adj neki nevet, és találd ki, mit tud!</p>
  {keszlet(ALKATRESZEK)}
  {lab(1)}
</section>
<section class="lap">
  <h1>Öt robot lépésről lépésre</h1>
  <p class="jel">Mindig azt rajzold, ami <i>piros</i>. Ami fekete, az már megvan. A&nbsp;negyedik kockában a&nbsp;kész robot látszik, a&nbsp;tiédet színezd, ahogy szeretnéd.</p>
  {lepesek(ROBOTOK, LEPESEK)}
  {lab(2)}
</section>
<section class="lap nagy">
  <h1>Harci felszerelés és pilótafülke</h1>
  <p class="alcim">Négy újabb dobás: mivel harcol a&nbsp;robotod, mit lő ki, hol ül benne a&nbsp;pilóta, és hogyan repül?</p>
  {keszlet(FELSZERELES)}
  <div class="szabalyok also">
    <div class="szabaly"><b>Hová ül a&nbsp;pilóta?</b>Az ablakban elég egy kis kör fejnek és egy ív vállnak. Rajzolj neki létrát vagy ajtót, hogy be tudjon szállni.</div>
    <div class="szabaly"><b>Lő és repül!</b>Lángcsóva a&nbsp;hajtómű alá, füstpamacs a&nbsp;cső végére, pár vonal a&nbsp;rakéta mögé, csillag oda, ahol talál.</div>
    <div class="szabaly"><b>Mekkora óriás?</b>Rajzolj a&nbsp;lába mellé egy kis embert, fát vagy házat. Minél kisebbek, annál nagyobbnak látszik a&nbsp;robot.</div>
  </div>
  <div class="terv">
    <div class="rajzhely"><span>Ide rajzold a&nbsp;saját harci robotodat!</span></div>
    <div class="adatok">
      <h2>A robotom adatlapja</h2>
      <p>Neve:</p><p>Fegyvere:</p><p>Pilótája:</p><p>Szuperereje:</p><p>Legnagyobb ellensége:</p>
    </div>
  </div>
  {lab(3)}
</section>
<section class="lap">
  <h1>Pilóta és négy harci gép</h1>
  <p class="jel">Itt is azt rajzold, ami <i>piros</i>. Az első sorban a&nbsp;pilóta van nagyban; a&nbsp;gépekben elég belőle a&nbsp;feje és a&nbsp;válla.</p>
  {lepesek(GEPEK, LEPESEK2)}
  {lab(4)}
</section>
</body></html>"""
open('rajzoljunk-robotot.html', 'w').write(html)
print('ok')
