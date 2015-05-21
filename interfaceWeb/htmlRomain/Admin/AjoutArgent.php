<?php
	$util1 = $_Post[username1];
	$util2 = $_Post[username2];
	$argent = $_Post[montant];
	
	$base = mysql_connect ('localhost', 'phpadmin', 'groseillenu');
			mysql_select_db ('Loutre', $base) ;
			// lancement de la requete de transaction
			$sql = "";
			mysql_query ($sql) or die ('Erreur SQL !'.$sql.'<br />'.mysql_error());
			
			if(mysql_num_rows($reponse)){
				echo "Il y a qqch";
			}
			else{
				//header('Location: /marie/Connexion.html');
			}

			mysql_close();

?>