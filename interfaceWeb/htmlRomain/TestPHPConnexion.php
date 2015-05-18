<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom entré : ".$_POST[username];
			
			$nom = $_POST[username];
			
			echo '<form method="post" action="/marie/Client/Client.html">
					<input type="hidden" name="nom" value="'.$nom.'">
				 </form>';
				
			header('Location: /marie/Client/Client.html'); 	
	?>
		
</html>