import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM etudiants WHERE id =1")
resultat = cursor.fetchone()

print(resultat)

cursor.close()
conn.close()