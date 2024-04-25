<?php

if ($_SERVER["REQUEST_METHOD"] == "GET") {
    
    $data = $_GET["data"];

    $file = fopen("wastewater.txt", "a");

    fwrite($file, $data . PHP_EOL);

    fclose($file);

    echo "Data written to file successfully!"; //notif to user, aka me, that it worked
} else {
    // error message if not GET 
    echo "Error: Only GET requests are allowed!";
}
?>



