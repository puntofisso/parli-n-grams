<?php


function dolast() {


$db = parse_ini_file("my.cnf");
$user = $db['user'];
$pass = $db['password'];
$name = $db['database'];
$host = $db['host'];



$sql = "SELECT string from updatestring";
$conn = new PDO("mysql:host=$host;dbname=$name", "$user", "$pass");
$q = $conn->query($sql);
try {
$result = $q->setFetchMode(PDO::FETCH_ASSOC);
} catch  (PDOException $pe) {
                die("Could not connect to the database:" . $pe->getMessage());
}
$out = "";
while ($r = $q->fetch()) {
$out = $r['string'];
}
echo $out;
}
?>
