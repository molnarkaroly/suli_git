<?php
/* LEKÉRDEZÉSEK
        1. Feladat: SELECT SUM(ber), MAX(ber) FROM `dolgozok`;
        2. Feladat: 
        3. Feladat: 
        4. Feladat: 
        5. Feladat: 
        */

        include ("connect.php");



        echo "<strong>1. Feladat</strong><br>";
        $sql = "SELECT SUM(ber) as osszes, MAX(ber) as max FROM `dolgozok`;";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
            echo "<b>Összes fizetés:</b> ". $row["osszes"]. "<br>";
            echo "<b>Legnagyobb fizetés:</b> ". $row["max"]. "<br>";
          }
        } else {
          echo "0 results";
        }





        echo "<br><strong>2. Feladat</strong><br>";
        echo "<b>Név     -     Bér </b>". "<br>";
        $sql = 'SELECT nev, ber FROM dolgozok INNER JOIN osztaly ON dolgozok.osztaly = osztaly.osztalykod WHERE osztaly != 6 AND dolgozok.nev LIKE "B%" OR dolgozok.nev LIKE "P%" ;';
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
            echo $row["nev"]. "    -    ". $row["ber"]. "<br>";
          }
        } else {
          echo "0 results";
        }
        echo "<br><strong>3. Feladat</strong><br>";
        $sql = "SELECT dolgozok.osztaly as oszt, SUM(ber) as osszes, AVG(ber) as atlag FROM dolgozok INNER JOIN osztaly ON dolgozok.osztaly = osztaly.osztalykod GROUP BY dolgozok.osztaly; ";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
            echo $row["oszt"]. "     -     ". $row["osszes"]."     -     ". $row["atlag"]. "<br>";
          }
        } else {
          echo "0 results";
        }

        echo "<br><strong>4. Feladat</strong><br>";
        $sql = "SELECT nev, osztaly.megnevezes as osztn FROM `dolgozok` INNER JOIN osztaly ON dolgozok.osztaly = osztaly.osztalykod ORDER BY nev ASC, ber DESC;";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
            echo $row["nev"]. "     -     ". $row["osztn"]. "<br>";
          }
        } else {
          echo "0 results";
        }
        echo "<br><strong>5. Feladat</strong><br>";
        $sql = 'SELECT dolgozok.azon as azon, dolgozok.nev as nev, dolgozok.osztaly as oszt, dolgozok.ber as ber FROM dolgozok WHERE dolgozok.ber < (SELECT AVG(ber) FROM dolgozok);';
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
            echo $row["azon"]. "     -     ". $row["nev"]. "     -     ". $row["oszt"]. "     -     ". $row["ber"]. "<br>";
          }
        } else {
          echo "0 results";
        }

        $conn->close();

?>

<!--
        -->
