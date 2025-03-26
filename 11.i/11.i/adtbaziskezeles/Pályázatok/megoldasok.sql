-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 1. feladat:


-- 3. feladat:


-- 4. feladat:


-- 5. feladat:


-- 6. feladat:

SELECT * FROM `szamla` WHERE koltsegtipusId= 'C1' AND `ertek`> 1E5;

-- 7. feladat:

SELECT szamlaszam, datum, ertek
FROM szamla
WHERE koltsegtipusId = 'A7'
ORDER BY ertek DESC
LIMIT 5;
-- 8. feladat:
SELECT k.megnevezes, SUM(s.ertek) AS "elszamolt osszeg", COUNT(s.id) AS "szamlak szama"
FROM szamla s
JOIN koltsegtipus k ON s.koltsegtipusId = k.id
GROUP BY k.megnevezes
ORDER BY "elszamolt osszeg" DESC;

-- 9. feladat:
SELECT p.id AS "palyazat", 
       (p.tervezetA + p.tervezetC) AS "keret", 
       (SUM(s.ertek) / (p.tervezetA + p.tervezetC)) * 100 AS "allapot"
FROM palyazat p
JOIN szamla s ON p.id = s.palyazatId
GROUP BY p.id;
