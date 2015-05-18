<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom entré : ".$_POST[username];
			
			echo '<form method="post" action="/Client/client.html"
					<input type="hidden" name="nom" value=$_POST[username]>
				 </form>';
				 
			include('Location: /marie/Client/Client.html');      
	?>
		
</html>