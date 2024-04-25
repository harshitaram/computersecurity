<!DOCTYPE html>
<html>
<head>
        <title>Blase's example of PHP URL parameters</title>
</head>
<body>
<?php
    $x = 5;
    echo("<a href='https://www.uchicago.edu'>An example</a> showing how PHP can produce HTML" . $x . " code that is then rendered by the browser.<br /><br />");
?>
Let's see how HTML and PHP mix. Here are your URL parameters:<br /><br />
<?php
    print_r($_REQUEST);
?>
<br /><br />
And let's look at a special example looking for just one URL parameter:<br /><br />
<?php
    if(isset($_GET['blase'])) {
        echo "URL parameter 'blase' has the following value: " . $_GET['blase'];
    }
    else {
        echo "URL parameter 'blase' does not exist";
    }
?>
</body>
</html>

