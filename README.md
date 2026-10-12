# Robotbajnokság

Tanulós robotjáték második osztályosoknak. A gyerek feladatokat old meg, a jó válaszokért tallért kap, a tallérból robotot vesz, alakít át és fejleszt, a robotok pedig az arénában megküzdenek egymással.

A játék egyetlen HTML-fájl, telepíteni nem kell: nyisd meg az `index.html`-t egy böngészőben. Az állás a böngészőben marad meg (localStorage), szerver nincs mögötte.

## Mi van benne

- **Garázs:** legfeljebb 12 robot. Az első ingyen van, a többi 25 tallér.
- **Feladatok:** matek, magyar, környezet vagy vegyes, egy kör tíz kérdés. Jó válasz 2 tallér, három jó után sorozatban 3, hibátlan körért 5 jutalom.
- **Műhely:** alkatrészcsere, átfestés, átnevezés, és a négy érték (erő, sebesség, páncél, okosság) fejlesztése.
- **Aréna:** támadás előtt a robot feladatot kap; jó válasz szuperütés, rossz válasz gyenge ütés. Gyári ellenfél ellen tallérért, két saját robottal barátságos meccsben.

## A tananyag

A kérdések a második osztály őszi anyagának szokásos témáiból készülnek, nem egy konkrét iskola tanmenetéből:

- **Matek:** összeadás és kivonás tízesátlépéssel 20-ig, kerek tízesek, kétjegyű és egyjegyű átlépés nélkül, pótlás, számszomszédok, tízes szomszédok, kisebb-nagyobb, páros-páratlan, tízesek és egyesek, sorozatok.
- **Magyar:** j vagy ly, rövid és hosszú magánhangzók, magánhangzó vagy mássalhangzó, betűrend, szótagszám, elválasztás, mondatvégi írásjel.
- **Környezet:** évszakok, hónapok, a hét napjai, őszi természet.

A feladatok a `robotjatek_sablon.html` „FELADATOK” részében vannak. A szólisták (`JLY`, `HOSSZ`, `ELVAL`, `MONDAT`, `TUDAS`) szabadon bővíthetők, új feladattípust a `MATEK`, `MAGYAR` vagy `VILAG` tömbbe lehet felvenni.

## Fájlok

| Fájl | Mire való |
|------|-----------|
| `index.html`, `robotbajnoksag.html` | a kész játék (a kettő azonos) |
| `robotgyar.html` | játék nélküli robotgenerátor: véletlen robot adatlappal |
| `rajzoljunk-robotot.pdf` | négyoldalas nyomtatható rajzlap, ugyanezekkel az alkatrészekkel |
| `general.py` | az alkatrészek rajzai és a rajzlap generátora |
| `robotgyar_general.py` | az alkatrészkészlet bővítése, illesztési pontok, a két HTML-oldal összerakása |
| `robotjatek_sablon.html`, `robotgyar_sablon.html` | a játék és a generátor forrása; ezeket kell szerkeszteni |

## Újragenerálás

A kész HTML-fájlokat ne szerkeszd kézzel, mert a generátor felülírja őket. Módosítás után:

```bash
python3 robotgyar_general.py
```

Ez a sablonokba beírja az alkatrészkészletet, és elkészíti az `index.html`, a `robotbajnoksag.html` és a `robotgyar.html` fájlt. A rajzlap PDF-jéhez a `rajzoljunk-robotot.html`-t kell Chrome-ból PDF-be nyomtatni.

## Ellenőrző mód

A játék címe után írt `?teszt=garazs`, `muhely`, `tanulas`, `felallas`, `arena` vagy `vege` rögtön az adott képernyőt nyitja meg hét próbarobottal; a `vege` magától végigjátszik egy harcot. A lap címében megjelenik, hogy kilóg-e valami a képernyőről.
