import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    AnimalName TEXT NOT NULL,
    AnimalType TEXT NOT NULL
)
"""
)

animals_data = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець"),
]

cursor.executemany(
    "INSERT INTO Animals (AnimalName, AnimalType) VALUES (?, ?)", animals_data
)
conn.commit()

cursor.execute(
    "UPDATE Animals SET AnimalName = 'Сокіл' WHERE AnimalName = 'Орел'"
)
conn.commit()

print("--- Звірі типу 'Ссавець': ---")
cursor.execute("SELECT * FROM Animals WHERE AnimalType = 'Ссавець'")
mammals = cursor.fetchall()
for row in mammals:
    print(f"ID: {row[0]}, Назва: {row[1]}, Тип: {row[2]}")

print("\n" + "=" * 40 + "\n")

print("--- Всі записи у таблиці 'Animals': ---")
cursor.execute("SELECT * FROM Animals")
all_animals = cursor.fetchall()
for row in all_animals:
    print(f"ID: {row[0]}, Назва: {row[1]}, Тип: {row[2]}")

conn.close()
