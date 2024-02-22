import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('kanji.db')
c = conn.cursor()

# Добавление новых столбцов
c.execute("ALTER TABLE kanji ADD COLUMN groop_id INTEGER DEFAULT 1")
c.execute("ALTER TABLE kanji ADD COLUMN place INTEGER")

# Заполнение столбца place значениями
c.execute("SELECT rowid FROM kanji")
rows = c.fetchall()
for i, row in enumerate(rows, start=1):
    c.execute("UPDATE kanji SET place = ? WHERE rowid = ?", (i, row[0]))

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
