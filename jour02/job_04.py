import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT nom, capacite FROM salles")
resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()