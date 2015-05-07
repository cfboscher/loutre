		<?php
			//On récupère les données entrées dans les champs
			$nom = $_POST['username'];
			$prenom = $_POST['prenom'];
			$mdp = $_POST['pass'];
			
			//On vérifie que les champs ne sont pas vides
			if(empty($nom))
			{
				//Choisir ce qu'il faut afficher
				exit();
			}
			
			elseif(empty(mdp))
			{
				//Choisir ce qu'il faut afficher
				exit();
			}
			
			elseif(empty($prenom))
			{
				//Choisir ce qu'il faut afficher
				exit();
			}
			//Si tout est bon on lance la requête SQL
			else
			{
				$db = mysql_connect('localhost', 'login', 'password');
				mysql_select_db('nomdelabase', $db);
				$sqlConnect = 'SELECT *FROM Personne WHERE UCASE(SUBSTR(Personne.Prenom, 0, 1)) = UCASE(SUBSTR($prenom,0,1))AND UCASE(SUBSTR(Personne.Nom,1)) = UCASE(SUBSTR($nom,1)) AND Personne.Password=$mdp';
				$reqConnect = mysql_query($sqlConnect);
			}
			
			$answer = $reqConnect->fetch();
			$role = $answer['Role'];
			$id = $answer['ID'];
		?>
			
		<html>
			if($role == 1)
			{
				<form method=POST action="/AdminPHP/Accueil.php">
				   <input type="hidden" name="IDAdmin" value=".$ID."></input>
				</form>
			}
			
			else
			{
			<form method=POST action="/ClientPHP/Client.php">
			   <input type="hidden" name="IDClient" value=".$ID."></input>
			   <input type="hidden" name="PrenomClient" value=".$prenom."></input>

			</form>
			}
		</html>	
			