"""
Примеры некоторых стандартных итерабельных объектов.
Пример 1: список
"""

# Список
my_list = [1, 2, 5, 7, 32, 148]

# Обход списка
for element in my_list:
    print(element)

# Функция enumerate возвращает итерабельный объект, который возвращает пары индекс-значение
for index, element in enumerate(my_list):
    print('my_list[{}] = {}'.format(index, element))

"""
Примеры некоторых стандартных итерабельных объектов.
Пример 2: строка
"""

# Строка
string = 'A string'

# Обход строки посимвольно
for char in string:
    print(char)

"""
Примеры некоторых стандартных итерабельных объектов.
Пример 3: диапазон
"""

# В Python 3 range -- это итерабельный объект, который задаёт диапазон.
# В Python 2 для этого служит xrange, а range является функцией,
# которая возвращает список.
my_range = range(2, 17, 2)

for counter in my_range:
    print(counter)

"""
Итерабельные объекты должны реализовывать как минимум один из двух методов:
 -  __iter__(self)
 -  __getitem__(self, key)

Метод __iter__ возвращает объект-итератор (будет рассмотрен далее).
Метод __getitem__ возвращает элемент контейнера по ключу или индексу.

Встроенная фукнция iter (автоматически вызывается циклом for) вызывает метод
__iter__, если он существует. Иначе, если существует метод __getitem__, то
автоматически создаётся итератор, который вызывает метод __getitem__ с
возрастающими индексами, начиная от нуля, до возникновения исключения
IndexError. Если объект не реализовавает ни один из этих методов, то данный
объект не является итерабельным и выбрасывается исключение TypeError.
"""


class SimpleIterable(object):
    """Класс итерабельного объекта с методом __getitem__"""

    def __getitem__(self, index):
        if 0 <= index < 5:
            return index * 2
        else:
            raise IndexError('iterable index out of range')


# Создание объекта
iterable = SimpleIterable()

# Вывод некоторых значений
print('iterable[0] =', iterable[0])
print('iterable[3] =', iterable[3])
print()

# Итерирование
for i in iterable:
    print(i)

"""
Итератор (iterator) – это объект, который представляет поток данных.
Повторяемые вызовы метода __next__() (next() в Python 2) итератора
или передача его встроенной функции next() возвращает последующие
элементы потока.

Если больше не осталось данных, выбрасывается исключение StopIteration.
После этого итератор исчерпан и любые последующие вызовы его метода __next__()
снова генерируют исключение StopIteration.

Итераторы обязаны иметь метод __iter__, который возвращает сам объект итератора.
Таким образом, любой итератор сам по себе также является итерабельным объектом.
"""


# Функция обхода итерабельного объекта
def traverse(iterable):
    print('Traversing {}:'.format(type(iterable).__name__))
    for element in iterable:
        print(element)
    print()


# Объявление списка
my_list = [1, 2, 3, 5, 8]

# Получение его итератора
list_iterator = iter(my_list)

# Обход списка
traverse(my_list)

# Обход итератора списка
traverse(list_iterator)

# Очередной обход списка -- работает корректно, так как создаётся
# новый объект-итератор
traverse(my_list)

# Очередной обход итератора -- не выводится ничего, так как
# элементы в итераторе уже исчерпаны
traverse(list_iterator)

"""
Пример создания итератора
"""

import math


class MyRange(object):
    """Итератор, который ведёт себя подобно встроенному классу range
    (за исключением того, что range является итерабельным объектом,
    а не итератором, и создаёт каждый раз новый итератор, так же как
    и список).
    """

    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        if step == 0:
            raise ValueError('step must not be zero')
        else:
            self.step = step

        length = math.ceil((self.end - self.start) / self.step)
        self.length = length if length >= 0 else 0

        self.elements_returned = 0
        self.current = None

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.elements_returned >= self.length:
            raise StopIteration

        self.elements_returned += 1

        if self.current is None:
            self.current = self.start
        else:
            self.current += self.step

        return self.current

    def __repr__(self):
        if self.start == 0 and self.step == 1:
            fmt = '{end}'
        elif self.step == 1:
            fmt = '{start}, {end}'
        else:
            fmt = '{start}, {end}, {step}'
        return 'MyRange({})'.format(fmt).format(start=self.start,
                                                end=self.end,
                                                step=self.step)


def test_len():
    """Функция тестирования метода len"""

    radius = 30

    try:
        for start in range(-radius, radius + 1):
            for end in range(-radius, radius + 1):
                for step in range(-radius, radius + 1):
                    if step == 0:
                        continue

                    my_range = MyRange(start, end, step)
                    std_range = range(start, end, step)

                    # Оператор assert проверяет, что заданное выражение
                    # истинно, и если нет, выбрасывает исключение AssertionError
                    assert len(my_range) == len(std_range)
    except AssertionError:
        print('Test failed')
        print('start =', start)
        print('end =', end)
        print('step =', step)
        print('len(my_range) =', len(my_range))
        print('len(std_range) =', len(std_range))
        print()
    else:
        print('__len__ tests passed normally')


def test_iterator():
    """Функция тестирования итератора"""

    radius = 30

    try:
        for start in range(-radius, radius + 1):
            for end in range(-radius, radius + 1):
                for step in range(-radius, radius + 1):
                    if step == 0:
                        continue

                    my_range = MyRange(start, end, step)
                    std_range = range(start, end, step)

                    # Получение списков значений
                    my_range_values = list(my_range)
                    std_range_values = list(std_range)

                    assert my_range_values == std_range_values
    except AssertionError:
        print('Test failed')
        print('start =', start)
        print('end =', end)
        print('step =', step)
        print('my_range_values =', my_range_values)
        print('std_range_values =', std_range_values)
        print()
    else:
        print('iter tests passed normally')


def main():
    # Простая проверка итератора
    for i in MyRange(10):
        print(i)

    print()

    # Использование итератора напрямую
    iterator = MyRange(2, 8, 2)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        print()

    # Тестирование метода __len__
    test_len()

    # Тестирование итератора
    test_iterator()


if __name__ == '__main__':
    main()

"""
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    # Повторный обход списка
    for element in my_list:
        print(element)


if __name__ == '__main__':
    main()
