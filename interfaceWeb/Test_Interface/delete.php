 <?
// pensez a ouvrir une connexion vers mysql ici
$db = mysql_connect('localhost','root','loutre');
mysql_select_db('testBD',$db);
// voir les exercices dans le menu de droite pour cela.

if(isset($_POST) && !empty($_POST['login'])) {
  extract($_POST);
  // on recupère le password de la table qui correspond au login du visiteur
  $sql ="DELETE FROM user WHERE login ='".$login."'";
  $req = mysql_query($sql);

  if($req){
	echo '<p>Requete effectuee avec succes.<p>';
	header('Location: admin.html');
	exit;
  }
  else{
	echo '<p>Erreur dans la requete.<p>';
	include('delete.html');
	exit;
  }
}
else {
  echo '<p>Vous avez oublié de remplir un champ.</p>';
   include('delete.html'); // On inclut le formulaire d'identification
   exit;
}


?>
