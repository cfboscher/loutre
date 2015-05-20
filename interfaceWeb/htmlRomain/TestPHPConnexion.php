<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom entré : ".$_POST[username];
			
			$nom = $_POST[username];
	?>
		<br>
		
		<form method="post" action="/marie/Client/Client.php">

			<p><input type="hidden" name="coucou" value="Marie"/></p>
			<input type="submit" value="Continuer">


		</form>
		
	
</html>