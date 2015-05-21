    <?php
	ini_set('display_errors', 1);
	error_reporting(E_ALL);
	
    // on se connecte à notre base
    $base = mysql_connect ('localhost', 'python', 'jambeo');
    mysql_select_db ('Loutre', $base) ;
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