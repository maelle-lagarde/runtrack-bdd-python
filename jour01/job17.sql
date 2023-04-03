mysql> UPDATE etudiants SET age = '20' WHERE id = 1;
Query OK, 1 row affected (0,00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM etudiants WHERE nom='Spaghetti';
+----+-----------+--------+-----+---------------------------------+
| id | nom       | prenom | age | email                           |
+----+-----------+--------+-----+---------------------------------+
|  1 | Spaghetti | Betty  |  20 | betty.Spaghetti@laplateforme.io |
+----+-----------+--------+-----+---------------------------------+
1 row in set (0,00 sec)