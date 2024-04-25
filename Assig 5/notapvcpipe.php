<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Restaurant Recommendation</title>
</head>
<body>
    <?php
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        $restaurantName = $_POST["restaurantName"];

        $file = fopen("restaurant_recommendations.txt", "a");

        fwrite($file, $restaurantName . PHP_EOL); //PHP_EOL = \n inspo: https://coderwall.com/p/qefb4w/use-the-php-constant-php_eol-to-print-the-correct-end-of-line-symbol-no-matter-what-system-you-re-on

        fclose($file);

        // Something so user knows their submission was recorded 
        echo "<h1>Thank you for your recommendation!</h1>";
    } else {
    ?>
    <h1>Submit Restaurant Rec</h1>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
        <label for="restaurantName">Restaurant Name:</label><br>
        <input type="text" id="restaurantName" name="restaurantName" required><br><br>
        <input type="submit" value="Submit">
    </form>
    <?php
    }
    ?>
</body>
</html>
