import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ml-031393",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("select SUM(capacite) FROM salles;")
resultat = cursor.fetchone()

print("La capacité de toutes les salles est de :", resultat[0])

cursor.close()
conn.close()