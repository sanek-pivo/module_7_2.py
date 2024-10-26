from pprint import pprint

def custom_write(file_name, strings):  # Создаём функцию custom_write (file_name, strings)
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')

    index = 1
    for string in strings:
        position = file.tell() # Получение номера байта начала строки используем метод tell()
        file.write(string + '\n')
        strings_positions[index] = (index, position), string
        index += 1

    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info) # Вывод на консоль:

for elem in result.values():
    print(elem)