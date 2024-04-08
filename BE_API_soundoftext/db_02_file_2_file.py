from googletrans import Translator
from datetime import datetime
import time

def translate_words():
    source_file_path = "C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/words_en_20k.txt"
    target_file_path = "C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/translated_words.txt"

    # Инициализация переводчика
    translator = Translator()

    try:
        with open(target_file_path, 'r', encoding='utf-8') as file:
            last_translated_word = file.readlines()[-1].split('\t')[1].split(' - ')[0]
    except Exception:
        last_translated_word = None

    start_translation = last_translated_word is None

    with open(source_file_path, 'r', encoding='utf-8') as file:
        english_words = file.read().splitlines()

    translated_count = 0

    with open(target_file_path, 'a', encoding='utf-8') as file:
        for word in english_words:
            if not start_translation and word == last_translated_word:
                start_translation = True
                continue
            if start_translation:
                try:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    translated_word = translator.translate(word, src='en', dest='ru').text
                    file.write(f"{current_time}\t{word} - {translated_word}\n")
                    print(f"{current_time}\t{word} - {translated_word}")
                    translated_count += 1
                    time.sleep(0.5)  # Пауза между запросами
                except Exception as e:
                    print(f"Ошибка при переводе слова '{word}': {e}")
                    break  # Прерываем цикл при возникновении ошибки
            if translated_count >= 1500:  # Приблизительное количество слов за 25 минут
                break

def main():
    while True:
        start_time = time.time()
        translate_words()
        elapsed_time = time.time() - start_time
        if elapsed_time < 1500:  # 25 минут = 1500 секунд
            time_to_wait = 1500 - elapsed_time
            print(f"Ожидание {time_to_wait} секунд до следующего перезапуска...")
            time.sleep(time_to_wait)

if __name__ == "__main__":
    main()
