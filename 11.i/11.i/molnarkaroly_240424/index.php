<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<p>Dolgozók</p>
<form action="upload.php" enctype="multipart/form-data" method="post">
    <input type="file" name="adatok">
    <input type="submit"value="Feltöltés">
</form>

<p>Osztályok</p>
<form action="upload2.php" enctype="multipart/form-data" method="post">
    <input type="file" name="adatok">
    <input type="submit"value="Feltöltés">
</form>

<p><b> <a href="feladat.php">Megoldások</a> </b></p>
</body>
</html>