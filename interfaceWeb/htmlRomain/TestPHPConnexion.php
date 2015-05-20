<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom d'utilisateur : ".$_POST[username];
			
			$nom = $_POST[username];
	?>
		<br>
		Si la page ne se charge pas au bout de 5 secondes, cliquez ici : <br>
		<form method="post" action="/marie/Client/Client.php">

			<p><input type="hidden" name="coucou" value="<?php echo $nom;?>"/></p>
			<input type="submit" value="Continuer">


		</form>
		
	
</html>