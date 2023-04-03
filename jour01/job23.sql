mysql> SELECT * FROM etudiants WHERE age = (SELECT MAX(age) FROM etudiants);
+----+-------+--------+-----+-----------------------------+
| id | nom   | prenom | age | email                       |
+----+-------+--------+-----+-----------------------------+
|  2 | Steak | Chuck  |  45 | chuck.steak@laplateforme.io |
+----+-------+--------+-----+-----------------------------+
1 row in set (0,00 sec)