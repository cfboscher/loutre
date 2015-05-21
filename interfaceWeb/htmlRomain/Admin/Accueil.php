<hmtl>
	<head>
		<title>Admin - LOUTRE</title>
		<link rel="stylesheet" href="../Ressources/styleLoutre.css" />
	</head>

	<body >
		<div id="logo">
			<img src="../Ressources/LogoLoutre - admin.jpg" alt="Logo Loutre" style="width:800px">
		</div>

		<div id="page-wrap">
			<h1>Bonjour admin, c'est l'heure de se mettre au travail!</h1>
		</div>
		
		<div id="page-wrap">
		<h2> Virement vers un utilisateur : </h2>
		<br>
				<form method="post" action="/AjoutArgent.php">
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