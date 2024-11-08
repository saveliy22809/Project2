def caesar_cipher(text, shift, action="encrypt"):
    """
    Функция для шифрования или дешифрования текста с поддержкой русского и английского алфавитов.

    Код на Python - сам алгоритм шифрования и дешифрования
    Данные - текст, сдвиг и тип действия
    Контроль - проверка действия (шифрование или дешифрование)
    """
    # Проверка действия и настройка сдвига
    if action == "decrypt":
        shift = -shift
    elif action != "encrypt":
        raise ValueError("Некорректное действие. Используйте 'encrypt' или 'decrypt'.")

    result = ""

    for char in text:
        # Проверка, является ли символ буквой
        if char.isalpha():
            # Проверка языка символа
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':  # Английский алфавит
                start = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - start + shift) % 26 + start)
            elif 'А' <= char <= 'Я' or 'а' <= char <= 'я':  # Русский алфавит
                start = ord('А') if char.isupper() else ord('а')
                new_char = chr((ord(char) - start + shift) % 32 + start)
            else:
                new_char = char
            result += new_char
        else:
            # M2: Добавление символов, не требующих шифрования
            result += char

    # Возврат результата шифрования/дешифрования
    return result


# Запрос ввода от пользователя
text = input("Введите текст для шифрования/дешифрования: ")
shift = int(input("Введите величину сдвига: "))
action = input("Выберите действие ('encrypt' для шифрования, 'decrypt' для дешифрования): ").strip().lower()

# Обработка данных и вывод результата
try:
    result = caesar_cipher(text, shift, action)
    if action == "encrypt":
        print("Зашифрованный текст:", result)
    elif action == "decrypt":
        print("Расшифрованный текст:", result)
except ValueError as e:
    print("Ошибка:", e)
