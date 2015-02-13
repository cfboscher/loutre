 <?
// pensez a ouvrir une connexion vers mysql ici
$db = mysql_connect('localhost','root', 'loutre');  // 1
mysql_select_db('testBD',$db); 
// voir les exercices dans le menu de droite pour cela.

if(isset($_POST) && !empty($_POST['login']) && !empty($_POST['pass'])) {
  extract($_POST);
  // on recupère le password de la table qui correspond au login du visiteur
  $sql = "select password from user where login='".$login."'";
  $req = mysql_query($sql) or die('Erreur SQL !<br>'.$sql.'<br>'.mysql_error());

  $data = mysql_fetch_assoc($req); 
if($data['password'] != $pass) {
    echo '<p>Mauvais login / password. Merci de recommencer</p>';
    include('index.html'); // On inclut le formulaire d'identification
    exit;
  }
  else {
    session_start();
    $_SESSION['login'] = $login;
    
    echo 'Vous etes bien logué.';
    // ici vous pouvez afficher un lien pour renvoyer
    // vers la page d'accueil de votre espace membres
    if($login=="nicolas"){
	header('Location: admin.html');
    }
    else{
	header('Location: user.html');
    }  
  }   
}
else {
  echo '<p>Vous avez oublié de remplir un champ.</p>';
   include('index.html'); // On inclut le formulaire d'identification
   exit;
}


?>
