	<?php
						
			echo "Nom d'utilisateur : ".$_POST[username];
			
			$nom = $_POST[username];
			$pass = $_POST[pass];
			
			if($nom == 'admin')
			{
				header('Location: /marie/Admin/Accueil.php');
			}
			
			$base = mysql_connect ('localhost', 'phpadmin', 'groseillenu');
			mysql_select_db ('Loutre', $base) ;
			// lancement de la requete
			$sql = "SELECT solde, nom FROM Personne WHERE Personne.nom='$nom'";
			mysql_query ($sql) or die ('Erreur SQL !'.$sql.'<br />'.mysql_error());
			
			if(mysql_num_rows($reponse)){
				echo "Il y a qqch";
			}
			else{
				header('Location: /marie/Connexion.html');
			}

			mysql_close();
	?>
	
<html>
	<head>
		<title>LOUTRE</title>
		<link rel="stylesheet" href="./Ressources/styleLoutre.css" />
	</head>
	
	<body >
			
		<div id="logo">
		
			<a href="../Connexion.html"><img src="./Ressources/LogoLoutre.jpg" alt="Logo Loutre" style="width:800px"></a>
		</div>

		<div id="page-wrap">
			<h1>Bonjour <?php echo $id['nom']; ?>, heureux de vous revoir!</h1>
			<h2>Il vous reste <?php echo $id['solde']; ?> groseilles sur votre compte.</h2>
		</div>

		<a href="/marie/Connexion.html"><button> Deconnexion </button></a><br>


	</body>
</html>