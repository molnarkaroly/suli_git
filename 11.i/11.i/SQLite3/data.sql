
DROP TABLE IF EXISTS tableee;
CREATE TABLE IF NOT EXISTS tableee (id INTEGER PRIMARY KEY,
  nev TEXT(12),
  nem TEXT(5),
  el TEXT(5),
  szul TEXT 
);


INSERT INTO tableee VALUES (1,'Fehér Hollo',True,True,'2023-04-13'),(2,'Bekre Pál',True,True,'2022-10-20'),(3,'Fekete Holló',True,'False','1800-11-02'),(4,'Ajtai Zafira','False',True,'2008-02-11');


