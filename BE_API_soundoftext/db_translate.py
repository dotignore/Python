import sqlite3
from googletrans import Translator
import time  # Для затримки між запитами

def translate_and_save(db_path, limit=100):
    translator = Translator()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Отримання перших слов з таблиці Words_en
    cursor.execute("SELECT Word FROM Words_en LIMIT ?", (limit,))
    words = cursor.fetchall()

    for word in words:
        try:
            # Переклад слова
            translated_text = translator.translate(word[0], src='en', dest='ru').text
            # Виведення слова та його перекладу
            print(f"'{word[0]}' перекладається як '{translated_text}'")
            # Вставка перекладеного слова в Words_ru
            cursor.execute("INSERT INTO Words_ru (Word, AccessCount, AudioPath) VALUES (?, 0, NULL)", (translated_text,))
            # Зберігання змін після кожного перекладу
            conn.commit()
            # Пауза на 0.5 секунди перед наступним перекладом
            time.sleep(0.5)
        except Exception as e:
            print(f"Помилка при перекладі слова {word[0]}: {str(e)}")
            # Якщо виникає помилка, продовжуємо з наступним словом
            continue

    # Закриття з'єднання з базою даних
    conn.close()

# Шлях до вашої бази даних
db_path = "C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/translate.db"
translate_and_save(db_path)
