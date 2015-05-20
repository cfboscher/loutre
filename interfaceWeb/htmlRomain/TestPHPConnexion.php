<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom d'utilisateur : ".$_POST[username];
			
			$nom = $_POST[username];
			$pass = $_POST[pass];
			
		// on se connecte à MySQL
		$db = mysql_connect('localhost', 'phpuser', 'lambda');

		// on sélectionne la base
		mysql_select_db('Loutre',$db);

		// on crée la requête SQL
		$sql = 'SELECT * FROM Personne WHERE UCASE(SUBSTR(Personne.Prenom, 0, 1)) = UCASE(SUBSTR($username,0,1)) AND UCASE(SUBSTR(Personne.Nom,1)) = UCASE(SUBSTR(username,1))';

		// on envoie la requête
		$req = mysql_query($sql) or die('Erreur SQL !<br>'.$sql.'<br>'.mysql_error());

		// on fait une boucle qui va faire un tour pour chaque enregistrement
		while($data = mysql_fetch_assoc($req))
			{
				// on affiche les informations de l'enregistrement en cours
				echo '<b>'.$data['nom'].' '.$data['prenom'].'</b> ('.$data['statut'].')';
				echo ' <i>date de naissance : '.$data['date'].'</i><br>';
				$identifiant = .$data[ID];
			}

		// on ferme la connexion à mysql
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