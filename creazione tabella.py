import pyodbc

# Stringa di connessione per MySQL tramite ODBC
# Nota: assicurati che il nome del driver corrisponda a quello installato sul tuo PC
# (di solito è "MySQL ODBC 8.x Driver" o simile)
conn_str = (
    "DRIVER={MySQL ODBC 9.7 Unicode Driver};"  # Sostituisci con la versione installata
    "SERVER=localhost;"
    "PORT=3306;"
    "DATABASE=mysql-database;"
    "USER=root;"
    "PASSWORD=mysql-password;"
)

try:
    # 1. Connessione
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # 2. Creazione della tabella
    create_table_query = """
    CREATE TABLE IF NOT EXISTS utenti (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100)
    )
    """
    cursor.execute(create_table_query)
    print("Tabella creata con successo.")

    # 3. Inserimento dati
    insert_query = "INSERT INTO utenti (nome, email) VALUES (?, ?)"
    dati = ("Mario Rossi", "mario.rossi@example.com")
    
    cursor.execute(insert_query, dati)
    
    # Conferma la transazione
    conn.commit()
    print("Dati inseriti correttamente con pyodbc!")

except pyodbc.Error as err:
    print(f"Errore di connessione: {err}")

finally:
    # 4. Chiusura
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("Connessione chiusa.")