1. feladat
SELECT nev, magassag, mez FROM `jatekos` ORDER BY nev ASC;

2. feladat
SELECT jegyzokonyv.be, jegyzokonyv.ki FROM jegyzokonyv INNER JOIN jatekos ON jatekos.mez = jegyzokonyv.mez WHERE jatekos.nev= "Víg Péter";

3.feladat
SELECT COUNT(jegyzokonyv.bjo) FROM jegyzokonyv INNER JOIN jatekos ON jatekos.mez = jegyzokonyv.mez WHERE jatekos.nev= "Magas Viktor";

4.feladat
SELECT COUNT(jegyzokonyv.bkis), COUNT(jegyzokonyv.bjo) FROM jegyzokonyv INNER JOIN jatekos ON jatekos.mez = jegyzokonyv.mez GROUP BY jatekos.mez;

5.feladat
SELECT jatekos.nev FROM jegyzokonyv INNER JOIN jatekos ON jatekos.mez = jegyzokonyv.mez WHERE jegyzokonyv.be BETWEEN "00:35:00" AND "00:40:00" AND poszt="irányító";
