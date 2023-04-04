import mysql.connector

class Employes:
    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "root"
        self.password = "Ml-031393"
        self.database = "LaPlateforme"
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def create(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def read(self, id):
        sql = "SELECT * FROM employes WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def update(self, id, nom=None, prenom=None, salaire=None, id_service=None):
        sql = "UPDATE employes SET "
        values = []
        if nom is not None:
            sql += "nom = %s, "
            values.append(nom)
        if prenom is not None:
            sql += "prenom = %s, "
            values.append(prenom)
        if salaire is not None:
            sql += "salaire = %s, "
            values.append(salaire)
        if id_service is not None:
            sql += "id_service = %s, "
            values.append(id_service)
        sql = sql[:-2] + " WHERE id = %s"
        values.append(id)
        self.cursor.execute(sql, tuple(values))
        self.connection.commit()
        return self.cursor.rowcount

    def delete(self, id):
        sql = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.rowcount

    def close(self):
        self.connection.close()

employes = Employes("localhost", "user", "password", "database")
new_employee = employes.create("Longour", "Constance", 3700, 1)
print("Nouvel employé créé avec l'ID :", new_employee)