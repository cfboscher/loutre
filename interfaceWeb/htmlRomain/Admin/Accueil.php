<hmtl>
	<head>
		<title>Admin - LOUTRE</title>
		<link rel="stylesheet" href="../Ressources/styleLoutre.css" />
	</head>

	<body >
		<div id="logo">
			<img src="../Ressources/LogoLoutre - admin.jpg" alt="Logo Loutre" style="width:800px">
		</div>

		<div id="menu">
			<ul id="onglets">
				<li class="active"><a href="Accueil.html"> Accueil </a></li>
				<li><a href="Evenements.html"> Evenements </a></li>
				<li><a href="Creation.html"> Créer un compte </a></li>
				<li><a href="Gestion.html"> Surveillance Comptes </a></li>
				<li><a href="Parametres.html"> Paramètres </a></li>
				<li><a href="../Connexion.html"> Se déconnecter </a></li>
			</ul>
		</div>

		<div id="page-wrap">
			<h1>Bonjour admin, c'est l'heure de se mettre au travail!</h1>
		</div>
		
		<div id="page-wrap">
		<h2> Virement vers un utilisateur : </h2>
		<br>
				<form>
				Montant : 
				<input type="text" name="montant">
				En provenance de :
				<input type="text" name="username2">
				Vers :
				<input type="text" name ="username2"><br>
				<input type="submit" value="Valider la transaction">
				</form>
		</div>

	</body>
</html>