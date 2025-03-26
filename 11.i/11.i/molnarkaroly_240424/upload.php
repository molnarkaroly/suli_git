<?php
    include ("connect.php");

    $sql = "DROP TABLE IF EXISTS dolgozok";
    $conn->query($sql);

    $sql = "CREATE TABLE dolgozok(azon INT, nev VARCHAR(100), osztaly INT, ber INT, PRIMARY KEY(azon));";
    if ($conn->query($sql)) {
        echo "Tábla létrehozva! <br>";
    }

    print <<< EOT
    <!DOCTYPE html>
    <html lang="hu">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
    EOT;

    if ($_FILES["adatok"]["error"] > 0){
        echo "Hiba: " . $$_FILES["adatok"]["error"] . "<br>";
    } else {
        echo "Feltöltés: ". $_FILES["adatok"]["name"] ."<br>";
        echo "Típus: ". $_FILES["adatok"]["type"] ."<br>";
        echo "Méret: ". ($_FILES["adatok"]["size"] / 1024) ."Kb<br>";
        echo "Tárolva itt: ". $_FILES["adatok"]["tmp_name"] ."<br>";
        if (file_exists("upload/".$_FILES["adatok"]["name"])) {
            echo "A ". $_FILES["adatok"]["name"] ." fájl már létezik.<br>";
        } else {
            move_uploaded_file($_FILES["adatok"]["tmp_name"],"upload/".$_FILES["adatok"]["name"]);
            echo "Végleg tárolva itt: upload/".$_FILES["adatok"]["name"]."<br>";
        }
    }

    echo "<br>";
    $path = "upload/".$_FILES["adatok"]["name"];
    $aline = @file($path);
    if (count($aline) > 0) {
        foreach($aline as $line_num => $line){
            if ($line_num != 0){
                $data = explode(";", $line);
                $sql = "INSERT INTO  dolgozok(azon, nev, osztaly, ber) VALUES ('$data[0]', '$data[1]', '$data[2]', '$data[3]')";
                $conn->query($sql);
            }
        }
    }
    echo '<p><b> <a href="index.php">Vissza</a> </b></p>';

    print"</body>
    </html>";
?>