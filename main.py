import sqlite3
import re

# Создаем подключение к базе данных (или создаем новую базу данных, если она не существует)
conn = sqlite3.connect('kanji.db')
c = conn.cursor()

# Удаляем старую таблицу (если вы уверены, что хотите это сделать)
c.execute('DROP TABLE IF EXISTS kanji_list')

# Создаем новую таблицу
c.execute('''
    CREATE TABLE kanji_list
    (KanjiID INTEGER PRIMARY KEY AUTOINCREMENT, Kanji text, Reading text, Meaning text, Examples text, ExamplesTranslate text)
''')


conn.commit()
conn.close()
