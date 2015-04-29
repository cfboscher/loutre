<hmtl>
	<head>
		<title>LOUTRE</title>
		<link rel="stylesheet" href="./Ressources/styleLoutre.css" />
	</head>

	<body >
		<div id="logo">
			<img src="./Ressources/LogoLoutre.jpg" alt="Logo Loutre" style="width:800px">
		</div>

		<div id="connexion">
			<h1>Bienvenue sur L.O.U.T.R.E.!</h1>
			<h2>Loutre est un Outil Unifié pour des Transactions Régulières Efficaces</h2>
		</div>

		<div id="connexion">
			<h2>Veuillez s'il vous plait vous connecter : </h2>
			nom:
			<br><input type="text" name="username">
			<br>
			mot de passe:<br><input type="password" name="pass">
			<br>
			
			<?php
			//On récupère les données entrées dans les champs
			$username = $_POST['username'];
			$mdp = $_POST['pass'];
			
			//On vérifie que les champs ne sont pas vides
			if(empty($name))
			{
				//Choisir ce qu'il faut afficher
				exit();
			}
			
			elseif(empty(mdp))
			{
				//Choisir ce qu'il faut afficher
				exit();
			}
			//Si tout est bon on lance la requête SQL
			else
			{
				$db = mysql_connect('localhost', 'login', 'password');
				mysql_select_db('nomdelabase', $db);
				$sqlConnect = 'SELECT *FROM Personne WHERE UCASE(SUBSTR(Personne.Prenom, 0, 1)) = UCASE(SUBSTR(##LOGIN##,0,1))AND UCASE(SUBSTR(Personne.Nom,1)) = UCASE(SUBSTR(##LOGIN##,1)) AND Personne.Password=##Hash du password##';
				$reqConnect = mysql_query($sqlConnect);
			}
			?>
			
			<button> Connexion </button>
		</div>
			<h3>Accès rapide (phase de tests):</h3>
			<a href="./Client/Client.html"><button> Client </button></a><br>
			<a href="./Admin/Accueil.html"><button> Admin </button></a>
		</div>		
	</body>
</html>