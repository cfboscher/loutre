    <?php
	ini_set('display_errors', 1);
	error_reporting(E_ALL);
	
    // on se connecte à notre base
    $base = mysql_connect ('localhost', 'python', 'jambeo');
    mysql_select_db ('Loutre', $base) ;
	// lancement de la requete
    $sql = 'INSERT INTO Personne(ID,Nom,Prenom,Role,Solde,Password) VALUES ('400609', 'Le', 'Marie', '0', '1', 'loutre' );
	mysql_close();
    ?>
    <html>
    <head>
    <title>Insertion de tibo dans la base</title>
    </head>
    <body>
    
	
    Tibo vient d'être inseré dans la base.
	
    </body>
    </html>