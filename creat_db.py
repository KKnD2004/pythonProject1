import sqlite3

conn = sqlite3.connect("date.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE date
                  (title text)
               """)