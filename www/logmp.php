<?php


$ngrams=$_GET['ngrams'];
$mp=$_GET['mp'];

$db = parse_ini_file("my.cnf");
$user = $db['user2'];
$pass = $db['password2'];
$name = $db['database'];
$host = $db['host'];

$conn = new PDO("mysql:host=$host;dbname=$name", "$user", "$pass");



        $sql = "INSERT INTO logs (ngrams,mp) VALUES (:ngrams, :mp)";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':ngrams', $ngrams, PDO::PARAM_STR);
        $stmt->bindParam(':mp', $mp, PDO::PARAM_STR);
        $stmt->execute();
?>
