<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom d'utilisateur : ".$_POST[username];
			
			$nom = $_POST[username];
			$pass = $_POST[pass];
	?>
		<br>
		Si la page ne se charge pas au bout de 5 secondes, cliquez ici : <br>
		<form method="post" action="/marie/Client/Client.php">

			<p><input type="hidden" name="name" value="<?php echo $nom;?>"/></p>
			<p><input type="hidden" name="value" value="<?php echo $pass;?>"/></p>

			<input type="submit" value="Continuer">


		</form>
		
	
</html>