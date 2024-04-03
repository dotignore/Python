import sqlite3

# Подключение к базе данных
conn = sqlite3.connect(r'C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\translate.db')
cursor = conn.cursor()

# Создание запроса для вставки данных
insert_query = "INSERT INTO Translations (en) VALUES (?)"

# Генерация и вставка значений от 1 до 466550
for i in range(1, 466551):
    cursor.execute(insert_query, (i,))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Данные успешно добавлены в колонку 'en'.")
