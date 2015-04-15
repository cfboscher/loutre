--------------------PHP

--Test de connexion. Si un tuple est retourné, alors la personne est connectée.
--Le champ Role représente le role de la personne (0 = utilisateur, 1=Admin)
--Stockez le champ ID en chiffré dans un cookie
SELECT *
FROM Personne
WHERE UCASE(SUBSTR(Personne.Prenom, 0, 1)) = UCASE(SUBSTR(##LOGIN##,0,1))
AND UCASE(SUBSTR(Personne.Nom,1)) = UCASE(SUBSTR(##LOGIN##,1))
AND Personne.Password=##Hash du password##

-- Consulter le solde
SELECT Solde
FROM Personne
WHERE UCASE(SUBSTR(Personne.Prenom, 0, 1)) LIKE UCASE(SUBSTR(##LOGIN##,0,1))
AND UCASE(SUBSTR(Personne.Nom,1)) LIKE UCASE(SUBSTR(##LOGIN##,1))
AND Personne.Password=##Hash du password##
--ou si vous avez l'ID du test de connexion
SELECT Solde
FROM Personne
WHERE ID=##ID de l etudiant##

--Ajouter/Supprimer du crédit (pour les admin)
INSERT INTO tab_transactions (ID_Etudiant,Montant)
VALUES (##ID de l étudiant##,##Montant à ajouter (positif ou négatif)##)

--Transferer du crédit entre utilisateurs
START TRANSACTION;
INSERT INTO tab_transactions (ID_Etudiant,Montant)
VALUES (##ID de l étudiant donneur ##,##Credit négatif##)
INSERT INTO tab_transactions (ID_Etudiant,Montant)
VALUES (##ID de l étudiant receveur ##,##Credit positif##)
COMMIT;

------------------PYTHON
--Consulter le solde
SELECT Solde
FROM Personne
WHERE ID=##ID de la carte##

--Débiter une boisson
INSERT INTO tab_transactions (ID_Etudiant,Montant)
VALUES (##ID de l étudiant##, SELECT - prix_boisson FROM parametres)