<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom entré : ".$_POST[username];
			
			echo '<form method="post" action="/marie/Client/Client.html">
					<input type="hidden" name="nom" value=$_POST[username]>
				 </form>';
				 
			header('Location: /marie/Client/Client.html');      
	?>
		
</html>