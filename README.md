# Cosa bisogna fare
1) apri docker HUB
2) cerca mysql:latest
3) aggiungere queste informazioni
	
	1) Nome database = mysql-server
	
	2) MYSQL_ROOT_PASSWORD=mysql-password
	
	3) MYSQL_DATABASE=mysql-database
	
	4) porte = 3306

# Alternativa da eseguire direttamente nel terminale
- docker run --name mysql-server -d -e MYSQL_ROOT_PASSWORD=mysql-password -e MYSQL_DATABASE=mysql-database -p 3306:3306 mysql:latest
