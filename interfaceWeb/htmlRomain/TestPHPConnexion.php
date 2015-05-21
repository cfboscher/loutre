<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
			ini_set('display_errors', 1);
			error_reporting(E_ALL);
						
			echo "Nom d'utilisateur : ".$_POST[username];
			
			$nom = $_POST[username];
			$pass = $_POST[pass];
			
			if($nom == 'admin')
			{
				header('Location: /marie/Admin/Accueil.html');
			}
			
			$base = mysql_connect ('localhost', 'phpadmin', 'groseillenu');
			mysql_select_db ('Loutre', $base) ;
			// lancement de la requete
			$sql = 'SELECT * FROM Personne';
			mysql_query ($sql) or die ('Erreur SQL !'.$sql.'<br />'.mysql_error());

			mysql_close();
	?>
	
		<br>
		Si la page ne se charge pas au bout de 5 secondes, cliquez ici : <br>
		<form method="post" action="/marie/Client/Client.php">

			<p><input type="hidden" name="name" value="<?php echo $nom;?>"/></p>
			<p><input type="hidden" name="identity" value="<?php echo $identifiant;?>"/></p>

			<input type="submit" value="Continuer">


		</form>
		
	
</html>