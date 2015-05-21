    <?php
	ini_set('display_errors', 1);
	error_reporting(E_ALL);
	
    // on se connecte à notre base
    $base = mysql_connect ('localhost', 'python', 'jambeo');
    mysql_select_db ('Loutre', $base) ;
    ?>
    <html>
    <head>
    <title>Insertion de tibo dans la base</title>
    </head>
    <body>
    <?php
    // lancement de la requete
    $sql = 'INSERT INTO Personne(ID,Nom,Prenom,Role,Solde,Password) VALUES ('400609', 'Le', 'Marie', '0', '1', 'loutre' );

    // on insere le tuple (mysql_query) et au cas où, on écrira un petit message d'erreur si la requête ne se passe pas bien (or die)
    mysql_query ($sql) or die ('Erreur SQL !'.$sql.'<br />'.mysql_error());

    // on ferme la connexion à la base
    mysql_close();
    ?>
	
    Tibo vient d'être inseré dans la base.
	
    </body>
    </html>