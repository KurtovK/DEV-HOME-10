import sqlite3

# Создание базы данных для таблицы рекордов
def create_table():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (name text, score integer)''')
    conn.commit()
    conn.close()

# Добавление результата игрока в таблицу
def add_record(name, score):
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute("INSERT INTO records VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

# Удаление результата игрока из таблицы
def delete_record(name):
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute("DELETE FROM records WHERE name=?", (name,))
    conn.commit()
    conn.close()

# Изменение результата игрока в таблице
def update_record(name, new_score):
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute("UPDATE records SET score=? WHERE name=?", (new_score, name))
    conn.commit()
    conn.close()

# Полная очистка таблицы
def clear_table():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute("DELETE FROM records")
    conn.commit()
    conn.close()

# Просмотр содержимого таблицы
def view_records():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute("SELECT * FROM records ORDER BY score DESC")
    records = c.fetchall()
    for record in records:
        print(record)
    conn.close()

# Отображение лучшей десятки
def view_top_ten():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    c.execute("SELECT * FROM records ORDER BY score DESC LIMIT 10")
    records = c.fetchall()
    for record in records:
        print(record)
    conn.close()
def execute_application():
    create_table()

    # Добавление результатов игроков
    add_record("Player 1", 100)
    add_record("Player 2", 200)
    add_record("Player 3", 150)

    # Изменение результата игрока
    update_record("Player 1", 120)

    # Удаление результата игрока
    delete_record("Player 2")

    # Просмотр содержимого таблицы
    view_records()

    # Отображение лучшей десятки
    view_top_ten()

    # Полная очистка таблицы
    clear_table()


if __name__ == '__main__':
    execute_application()