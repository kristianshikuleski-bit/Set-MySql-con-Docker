import pyodbc

# Stringa di connessione (assicurati che il nome del driver corrisponda al tuo sistema)
conn_str = (
    "DRIVER={MySQL ODBC 9.7 Unicode Driver};"
    "SERVER=localhost;"
    "PORT=3306;"
    "DATABASE=mysql-database;"
    "USER=root;"
    "PASSWORD=mysql-password;"
)

try:
    # 1. Connessione al database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # 2. Esecuzione della query di selezione
    query = "SELECT id, nome, email FROM utenti"
    cursor.execute(query)

    # 3. Recupero dei dati
    risultati = cursor.fetchall()

    # Stampa dei risultati
    print("-" * 40)
    print(f"{'ID':<5} | {'NOME':<15} | {'EMAIL'}")
    print("-" * 40)
    
    if not risultati:
        print("La tabella è vuota.")
    else:
        for riga in risultati:
            # riga[0] è l'ID, riga[1] è il nome, riga[2] è l'email
            print(f"{riga[0]:<5} | {riga[1]:<15} | {riga[2]}")
            
    print("-" * 40)

except pyodbc.Error as err:
    print(f"Errore durante la connessione o la lettura: {err}")

finally:
    # 4. Chiusura della connessione
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("Connessione chiusa.")