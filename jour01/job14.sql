mysql> SELECT * FROM etudiants WHERE age BETWEEN 18 AND 25 ORDER BY age ASC;
+----+-----------------+----------+-----+---------------------------------+
| id | nom             | prenom   | age | email                           |
+----+-----------------+----------+-----+---------------------------------+
|  3 | John Doe        | John     |  18 | john.doe@laplateforme.io        |
|  6 | Dupuis          | Martin   |  18 | martin.dupuis@laplateforme.io   |
|  5 | Dupuis          | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  1 | Betty Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io |
+----+-----------------+----------+-----+---------------------------------+