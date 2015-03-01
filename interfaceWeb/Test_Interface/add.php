 <?
// pensez a ouvrir une connexion vers mysql ici
$db = mysql_connect('localhost','root','loutre');
mysql_select_db('testBD',$db);
// voir les exercices dans le menu de droite pour cela.

if(isset($_POST) && !empty($_POST['login']) && !empty($_POST['credit'])  && !empty($_POST['password'])) {
  extract($_POST);
  // on recupère le password de la table qui correspond au login du visiteur
 // $sql ="INSERT INTO user VALUES('c',5,'ff')";
$sql = "INSERT INTO `testBD`.`user` (`login`, `Credit`, `password`) VALUES (\'C\', \'4\', \'h\');";  
$req = mysql_query($sql) or die('<br>'.$sql.'<br>'.mysql_error());
  
  if($req){
	echo '<p>Requete effectuee avec succes.<p>';
	//header('Location: admin.html');
	//exit;
  }
  else{
	echo '<p>Erreur dans la requete.<p>';
	include('add.html');
	exit;
  }
}
else {
  echo '<p>Vous avez oublié de remplir un champ.</p>';
   include('add.html'); // On inclut le formulaire d'identification
   exit;
}


?>
