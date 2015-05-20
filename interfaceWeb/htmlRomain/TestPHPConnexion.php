<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom entré : ".$_POST[username];
			
			$nom = $_POST[username];
	?>
		<br>
		
		<form method="post" action="/marie/Client/Client.html">

			<p><input type="hidden" name="coucou" value="Marie"/></p>

		</form>
		
	   <a href="/marie/Client/Client.html>Cliquez pour continuer...</a> 
	
</html>