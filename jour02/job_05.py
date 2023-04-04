import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ml-031393",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("select SUM(superficie) as superficie_totale from etage;")
resultat = cursor.fetchone()

print("La superficie de La Plateforme est de", resultat[0], "m2.")

cursor.close()
conn.close()