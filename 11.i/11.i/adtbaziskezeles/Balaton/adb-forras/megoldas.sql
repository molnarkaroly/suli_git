
-- 10.feladat
DELETE FROM klubok WHERE `klubok`.`klubNev`='ZZZ';

-- 11.feladat
UPDATE `klubok` SET `klubNev` = 'ADMIRAL' WHERE `klubok`.`id` = 1;


-- 12.feladat
SELECT AVG(pontok) AS AtlagPont FROM `hajok`;


-- 13.feladat
SELECT klubNev FROM `klubok` WHERE klubNev LIKE '___' ORDER BY klubNev DESC;

-- 14.feladat
SELECT kormanyosNev , hajoNev FROM `hajok` WHERE kormanyosNev LIKE "% István";


-- 15.feladat
SELECT COUNT(*) AS hajokSzama FROM `hajok` WHERE ido IS NULL;


-- 16.feladat
SELECT hajok.ido, osztalyok.osztalyNev, hajok.hajoNev FROM `hajok` INNER JOIN osztalyok ON hajok.hajoOszt = osztalyok.id WHERE ido IS NOT NULL GROUP BY ido ASC LIMIT 15;
