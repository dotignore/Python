from googletrans import Translator, LANGUAGES

translator = Translator()


def translate_file(input_file_path, output_file_path, src_lang='en', dest_lang='ru'):
    # Читаем исходный файл
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Поскольку есть ограничение на объем текста, разбиваем его на части
    # Примечание: этот пример не включает логику разбиения, но вы должны учитывать ограничения API
    parts = [text[i:i + 5000] for i in range(0, len(text), 5000)]  # Пример разбиения текста на части
    translated_parts = []

    for part in parts:
        # Перевод каждой части и добавление её в список
        translated = translator.translate(part, src=src_lang, dest=dest_lang)
        translated_parts.append(translated.text)

    # Соединяем переведенные части и записываем в выходной файл
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(''.join(translated_parts))


# Замените 'input.txt' и 'output.txt' на ваши пути к файлам
translate_file('C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/words_en.txt', 'C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/words_ru.txt')
