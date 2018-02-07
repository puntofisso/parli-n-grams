<?php

$ngram=$_GET['ngram'];
$mp=$_GET['mp'];
if (($ngram=="") || !isset($ngram) || ($mp=="") || !isset($mp)) {

echo "Error";
die();
}


try {
if ($mp=='all') {
$sql = "SELECT n.*, y.count as yearcount FROM ngrams n, yearcounts y  WHERE ngram ='".$ngram."' AND n.year = y.year ORDER by year asc";
} else {

$mparr = explode("|", $mp);
$mpjoined = join(",", $mparr);
$sql = "SELECT n.year, ngram, sum(n.count) as count, sum(y.count) as yearcount, $mp as mpstring FROM `ngramsmp` n, `yearcountsmp` y
WHERE n.year = y.year 
AND n.mp in (".$mpjoined.")
AND y.mp = n.mp 
AND ngram = '".$ngram."'
Group by year
Order by year asc";

// $sql = "SELECT n.*, y.count as yearcount FROM ngramsmp n, yearcountsmp y  WHERE ngram ='".$ngram."' AND n.year = y.year AND n.mp = '".$mp."' AND y.mp = n.mp ORDER by year asc";
}
$db = parse_ini_file("my.cnf");
$user = $db['user'];
$pass = $db['password'];
$name = $db['database'];
$host = $db['host'];


$conn = new PDO("mysql:host=$host;dbname=$name", "$user", "$pass");


$q = $conn->query($sql);
$result = $q->setFetchMode(PDO::FETCH_ASSOC);
} catch  (PDOException $pe) {
                die("Could not connect to the database:" . $pe->getMessage());
}

$out = array();
while ($r = $q->fetch()) {
$out[$r['year']] = $r;
}



echo json_encode($out);

?>
