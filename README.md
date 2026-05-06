# Cosa bisogna fare
1) apri docker HUB
2) cerca mysql:latest
3) aggiungere queste informazioni
	
	3) Nome database = mysql-server
	
	4) MYSQL_ROOT_PASSWORD=mysql-password
	
	5) MYSQL_DATABASE=mysql-database
	
	6) porte = 3306

# Alternativa da eseguire direttamente nel terminale
- docker run --name mysql-server -d -e MYSQL_ROOT_PASSWORD=mysql-password -e MYSQL_DATABASE=mysql-database -p 3306:3306 mysql:latest
