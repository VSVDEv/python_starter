"""Пример открытия файла для чтения"""


def read_file(fname):
    """Функция для чтения файла fname
    и вывода его содержимого на экран
    """

    # Открытие файла для чтения
    file = open(fname, 'r')

    # Вывод названия файла
    print('File ' + fname + ':')

    # Чтение содержимого файла построчно
    for line in file:
        # Вывод строки s.  Перевод строки в файле сохраняется в строке, поэтому
        # выводим без дополнительного перевода строки.
        print(line, end='')

    # Закрытие файла
    file.close()


if __name__ == '__main__':
    read_file('data/file.txt')

"""Пример использования функции os.path.join
для построения пути к файлу"""

# Модуль, который содержит функции для работы с путями в файловой системе
import os.path


def read_file(fname):
    """Функция для чтения файла fname
    и вывода его содержимого на экран
    """

    # Открытие файла для чтения
    file = open(fname, 'r')

    # Вывод названия файла
    print('File ' + fname + ':')

    # Чтение содержимого файла построчно
    for line in file:
        # Вывод строки s.  Перевод строки в файле сохраняется в строке, поэтому
        # выводим без дополнительного перевода строки.
        print(line, end='')

    # Закрытие файла
    file.close()


if __name__ == '__main__':
    # Функция os.path.join соединяет части пути в файловой системе требуемым
    # для данной платформы разделителем
    read_file(os.path.join('data', 'file.txt'))

"""Пример записи данных в текстовый файл"""

import os.path

text = '''Hello!
I am a text file. And I had been written with a Python script
before you opened me, so look up the docs and try to delete
me using Python, too.
'''


def write_text_to_file(filename, text):
    """Функция для записи в	файл filename строки text"""

    # Открытие файла для записи
    f = open(filename, "w")
    # Запись строки text в файл
    f.write(text)
    # Закрытие файла
    f.close()


if __name__ == '__main__':
    write_text_to_file(os.path.join('data', 'example02.txt'), text)

"""Использование оператора with для автоматического закрытия файла"""

import os.path

# Построение имени файла
filename = os.path.join('data', 'file.txt')

# Оператор with автоматически закроет файл при окончании выполнения операторов
# внутри него или возникновении исключения
with open(filename) as file:
    print(file.read())

"""Пример открытия текстового файла для чтения
с указанием кодировки"""

# __file__ - это атрибут модуля, в котором хранится имя его файла
# исходного кода
with open(__file__, 'r', encoding='utf-8-sig') as file:
    for number, line in enumerate(file):
        print('{0}\t{1}'.format(number + 1, line), end='')

print()

"""Пример открытия файла для чтения и записи"""

import os.path
import statistics
import datetime


def calculate_stats(filename):
    with open(filename, 'r+') as file:
        numbers = [float(line) for line in file.readlines()
                   if line != '\n' and not line.lstrip().startswith('#')]

        sum_ = sum(numbers)
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)

        cur_time = datetime.datetime.now()

        fmt = '\n' \
              '# Статистика от {time!s}\n' \
              '# Сумма:    {sum}\n' \
              '# Медиана:  {median}\n' \
              '# Среднее:  {mean}'

        print(fmt.format(time=cur_time,
                         mean=mean,
                         median=median,
                         sum=sum_),
              file=file)


if __name__ == '__main__':
    filename = os.path.join('data', 'example05.txt')
    calculate_stats(filename)

"""Пример открытия файла для дозаписи"""

import os.path
import datetime

log_file = os.path.join('data', 'ex06_log.txt')
with open(log_file, 'a') as log:
    print(datetime.datetime.now(), file=log)

"""Пример перезаписи файла"""

import os.path

filename = os.path.join('data', 'example07.txt')

# Чтение файла
with open(filename, 'r') as file:
    lines = file.readlines()

# Модификация данных
lines.insert(2, 'inserted line\n')

# Перезапись файла
with open(filename, 'w') as file:
    file.writelines(lines)

"""Пример использования файлового объекта io.StringIO"""

import io

# Создание потока
stream = io.StringIO()  # или io.StringIO('начальное значение')

# Запись данных в поток
stream.write('asdf in memory')

# Получение строки из объекта StringIO
print(stream.getvalue())

# Вывод текущей позиции
print('Current position:', stream.tell())

# Переход в начало потока
stream.seek(0)

# Запись данных в поток
stream.write('data')

# Вывод текущей позиции
print('Current position:', stream.tell())

# Чтение оставшихся данных в потоке
print(stream.read())

# Вывод текущей позиции
print('Current position:', stream.tell())

# Получение строки из объекта StringIO
print(stream.getvalue())

"""Пример использования бинарного файла"""

from array import array
import os.path

prefix = os.path.join('data', 'ex09_')

# Создание списка чисел
numbers = list(range(300, 400))

# Запись в текстовый файл
with open(prefix + 'text.txt', 'w') as txt_file:
    print(numbers, file=txt_file)

# Создание массива, поддеживающего buffer protocol, из списка
numbers_array = array('i', numbers)

# Запись в бинарный файл
binary_filename = prefix + 'binary.bin'
with open(binary_filename, 'wb') as bin_file:
    bin_file.write(numbers_array)

# Подготовка массива
filesize = os.path.getsize(binary_filename)  # размер файла
int_len = array('i').itemsize  # размер одного элемента в байтах
read_array = array('i', (0 for _ in range(filesize // int_len)))

# Чтение из бинарного файла
with open(binary_filename, 'rb') as file:
    file.readinto(read_array)  # чтение в массив

# Вывод массива на экран
print(read_array)

# Проверка, что считанные данные соответствуют изначальным
print(read_array.tolist() == numbers)

"""Пример использования json"""

import json
import os.path

data = [
    {
        'name': 'John',
        'age': 20,
    },
    {
        'name': 'Mary',
        'age': 19
    }
]

filename = os.path.join('data', 'example10.json')

# Сериализация
with open(filename, 'w') as file:
    json.dump(data, file)

# Десериализация
with open(filename, 'r') as file:
    read_data = json.load(file)
print(read_data)

"""Пример сериализации при помощи pickle"""

import os.path
import pickle
import reprlib


class Person(object):
    """Класс, описывающий человека"""

    def __init__(self, name, age, sibling=None):
        """Конструктор класса.

        Параметры:
            name    -- имя
            age     -- возраст
            sibling -- брат или сестра
        """
        self.name = name
        self.age = age
        self.sibling = sibling

    # Декоратор reprlib.recursive_repr(fillvalue='...') отслеживает рекурсивные
    # вызовы метода __repr__ и не даёт ему войти в бесконечную рекурсию,
    # возвращая fillvalue вместо вызовов данного метода, которые ещё не
    # завершены.
    @reprlib.recursive_repr()
    def __repr__(self):
        """Строковое представление объекта"""
        return 'Person({name!r}, {age!r}, {sibling!r})'.format(**self.__dict__)


def write_data(filename):
    """Функция создания и записи данных"""

    james = Person('James', 20)
    julia = Person('Julia', 21)
    james.sibling = julia  # создание циклических ссылок
    julia.sibling = james

    # Сериализация списка объектов
    with open(filename, 'wb') as file:  # 'wb' -- запись бинарного файла
        pickle.dump([james, julia], file)


def read_data(filename):
    """Функция чтения и вывода данных на экран"""

    # Десериализация
    with open(filename, 'rb') as file:
        data = pickle.load(file)

    # Вывод в консоль
    print(data)


if __name__ == '__main__':
    filename = os.path.join('data', 'example11.pkl')
    write_data(filename)
    read_data(filename)
