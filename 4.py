import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')  # Создаем соединение с базой данных
    c = conn.cursor()  # Получаем объект курсора для выполнения SQL команд

    # Создаем таблицу users
    c.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            isFavorite INTEGER
        )
    """)

    # Создаем таблицу dicts
    c.execute("""
        CREATE TABLE dicts (
            id INTEGER PRIMARY KEY,
            uid INTEGER,
            name TEXT NOT NULL,
            words TEXT NOT NULL,
            another_unknown_field INTEGER,
            FOREIGN KEY (uid) REFERENCES users (id)
        )
    """)

    conn.commit()  # Сохраняем изменения
    conn.close()  # Закрываем соединение

create_db()
    