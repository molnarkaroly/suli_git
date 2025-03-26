<?php
    $server = "localhost";
    $user = "root";
    $password = "";
    $databases = "dolgozat";


    $conn = mysqli_connect($server, $user, $password, $databases);

    if ("".$conn -> connect_error)
    {
        die("Connect error:". $conn -> connect_error);
    }
    else{
        echo " ";
    }

?>