import sqlite3

# Создайте подключение к вашей базе данных
con = sqlite3.connect('database.db')

# Создайте курсор для выполнения SQL-команд
cur = con.cursor()

# Создайте новую таблицу с именем sessions
cur.execute('''
CREATE TABLE sessions
(sid TEXT PRIMARY KEY,
expires DATETIME,
session TEXT)
''')

# Завершите транзакцию
con.commit()

# Закройте подключение
con.close()
