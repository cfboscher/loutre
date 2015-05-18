<html>	

	<head>
		<title>LOUTRE</title>
	</head>
	
	<?php
						
			echo "Nom entré : ".$_POST[username];
			
			echo '<form method="post" action="/marie/Client/Client.html">
					<input type="hidden" name="nom" value="<?php echo $_POST[username]; ?>">
				 </form>';
				      
	?>
		
</html>