import mysql.connector

class Animal:
    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "zoo"
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def create(self, nom, race, id_cage, date_naissance, pays_origine):
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s);"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def read(self, id):
        sql = "SELECT * FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def update(self, id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        sql = "UPDATE animal SET "
        values = []
        if nom is not None:
            sql += "nom = %s, "
            values.append(nom)
        if race is not None:
            sql += "race = %s, "
            values.append(race)
        if id_cage is not None:
            sql += "id_cage = %s, "
            values.append(id_cage)
        if date_naissance is not None:
            sql += "date_naissance = %s, "
            values.append(date_naissance)
        if pays_origine is not None:
            sql += "pays_origine = %s, "
            values.append(pays_origine)
        sql = sql[:-2] + " WHERE id = %s"
        values.append(id)
        self.cursor.execute(sql, tuple(values))
        self.connection.commit()
        return self.cursor.rowcount

    def delete(self, id):
        sql = "DELETE FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.rowcount

    def animals_in_zoo(self):
        sql = "SELECT * FROM animal"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def animals_in_cages(self):
        sql = "SELECT animal.nom, cage.id FROM animal JOIN cage ON animal.id_cage = cage.id"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def superficie(self):
        sql = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def close(self):
        self.connection.close()

animal = Animal("host", "user", "password", "database")
# ajoute un nouvel animal.
new_animal = animal.create("Tintin", "Suricate", 1, "2021-04-04", "Afrique")
print("Nouvel animal crée avec l'ID :", new_animal)

# supprimer un animal.
delete_animal = animal.delete(3)
print(f"L'animal avec l'ID {delete_animal} est parti dans un sanctuaire animal car les animaux dans les zoo c'est mal.")

# modifie les animaux.
update_animal = animal.update(4, "Tintin", "Suricate", 1, "2021-04-04", "Kenya")
print(f"L'animal avec l'ID {update_animal} a été mis à jour.")

# affiche tous les animaux dans le zoo.
display_animals = animal.animals_in_zoo()
print(f"Voici les animaux présents dans le zoo: {display_animals}")

# affiche tous les animaux avec leurs cages dans le zoo.
display_animals_cages = animal.animals_in_cages()
print(f"Voici les animaux au zoo ainsi que leurs cages : {display_animals_cages}")

# affiche la superficie totale du zoo.
superficie_cages = animal.superficie()
print(f"La superficie totale du toutes les cages est de {superficie_cages} m2.")