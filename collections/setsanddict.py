"""Создание множеств.
Все созданные здесь объекты являются экземплярами класса set
"""

my_set = {1, 5, 3, 9}  # множество целых чисел
print(my_set)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # множество строк
print(basket)  # дубликаты удалились


"""Пример создания множеств при помощи включений множеств
(аналогично списковым включениям).
Эти объекты также имеют тип set
"""

number_set = {i + j for i in range(10) for j in range(5)}
print(number_set)

char_set = {x for x in 'abracadabra' if x not in 'abc'}
print(char_set)


"""Использование конструкторов"""

# Пустое множество
empty_set = set()
print(empty_set)

# Пустое неизменяемое множество
empty_frozenset = frozenset()
print(empty_frozenset)

# Создание множеств из итерабельых объектов

my_frozenset = frozenset([4, 1, 3, 8])
my_set = set(my_frozenset)
print(my_set)
print(my_frozenset)

def get_ints(n):
    for i in range(n):
        yield i
        yield i + 1

print(list(get_ints(10)))  # все числа, возвращаемые генератором
print(set(get_ints(10)))   # множество содержит лишь уникальные значения


"""Операции с множествами (set и frozenset)"""

my_set = {4, 5, 1, 2}

# Количество элементов множества
print('len({}) = {}'.format(my_set, len(my_set)))

print()

# Проверка вхождения элемента
print(4 in my_set)
print(3 not in my_set)
print(9 in my_set)

print()

# Пересекаются ли множества
print({3, 4, 5}.isdisjoint({8, 1, 0}))
print({3, 4, 5}.isdisjoint({1, 2, 3}))

print()

# Проверка включения одного множества в другое
print({1, 7, 9}.issubset({1, 2, 3, 7, 9}))
print({1, 7, 9} <= {1, 2, 3, 7, 9})
print({1, 7, 9, 2, 3} <= {1, 2, 3, 7, 9})

print()

# Проверка строгого включения
print({1, 7, 9} < {1, 2, 3, 7, 9})
print({1, 7, 9, 2, 3} < {1, 2, 3, 7, 9})

print()

# Проверка включения одного множества в другое
print({1, 2, 3, 4}.issuperset({1, 2}))
print({1, 2, 4, 4} >= {1, 2})
print({1, 2, 3, 4} >= {1, 2, 3, 4})

print()

# Проверка строгого включения
print({1, 2, 4, 4} > {1, 2})
print({1, 2, 3, 4} > {1, 2, 3, 4})

print()

# Объединение множеств
print({1, 3}.union({2, 3, 4}))
print({1, 3} | {2, 3, 4})

print()

# Пересечение множеств
print({1, 3}.intersection({2, 3, 4}))
print({1, 3} & {2, 3, 4})

print()

# Разница множеств
print({1, 2, 3, 4}.difference({3, 4, 5}))
print({1, 2, 3, 4} - {3, 4, 5})

print()

# Симметрическая разница
print({1, 2, 3, 4}.symmetric_difference({3, 4, 5, 6}))
print({1, 2, 3, 4} ^ {3, 4, 5, 6})

print()

# Копирование множества
my_set = set('chars')
copy = my_set.copy()
print(copy)


"""Операции над множествами, которые являются методами, принимают в качестве
аргументов любые итерабельные объекты. Операции над множествами, записанные
в виде бинарных операций, требуют, чтобы второй операнд операции тоже был
множеством, и возвращают множество того типа, которым было первое множество
"""

print(frozenset('abc').union(frozenset('cdef')))  # корректно
print(frozenset('abc') | frozenset('cdef'))  # корректно
print(frozenset('abc').union('cdef'))  # корректно
# print(frozenset('abc') | 'cdef')  # ошибка



"""Операции с изменяемыми множествами (set)"""

my_set = {1, 3, 5}

my_set.update({2, 3, 4})  # my_set |= {2, 3, 4}
print(my_set)

my_set.intersection_update({0, 1, 2, 3, 10})  # my_set &= {0, 1, 2, 3, 10}
print(my_set)

my_set.difference_update({1})  # my_set -= {1}
print(my_set)

my_set.symmetric_difference_update({3, 4})  # my_set ^= {3, 4}
print(my_set)

my_set.add(5)  # my_set |= {5}
print(my_set)

my_set.remove(2)  # my_set -= {2}, но выбрасывает KeyError, если такого элемента нет
print(my_set)

my_set.discard(2)  # my_set -= {2}
print(my_set)

print(my_set.pop())
print(my_set)

my_set.clear()
print(my_set)


"""Проверка множеств на равенство происходит поэлементно,
независимо от типов множеств.
"""

print({1, 2, 3} == frozenset([1, 2, 3]))
print(set('abc') == frozenset('abc'))
print(set('abc') in set([frozenset('abc')]))





"""Создание словарей"""

# Все эти примеры создают одинаковые словари
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

# Те, кто имел опыт программирования на Си-подобных языках, могут
# подумать, что в этой строке ошибка (потому что в них операции
# сравнения связывались бы слева направо), однако в Python такое
# сравнение абсолютно корректно и действительно проверяет все
# значения на равенство друг другу. Здесь действуют те же правила,
# что мы рассматривали для двойных сравнений во втором уроке
# курса Python Starter (все последовательные операции сравнения
# и проверки равенства объединяются при помощи операции and).
print(a == b == c == d == e)

print(a)

print()

# Использование включений словарей (аналогично списковым включениям)
print({string: string.upper() for string in ('one', 'two', 'three')})



# Подобно тому, как можно передавать в функции произвольное количество
# позиционных аргументов, которые сохраняются в кортеже, можно передавать
# произвольное количество именованных аргументов, которые сохраняются в
# словаре. Для этого перед именем данного словаря в списке формальных
# параметров ставится два символа **. Если используются оба способа передачи
# произвольного количества аргументов, параметр в форме **kwargs в сигнатуре
# функции должен идти после параметра в форме *args.

def function(**kwargs):
    print(kwargs)


function(arg1='value1', arg2='value2')


# Аналогично можно и распаковывать любые отображения
# в именованные параметры при вызове функции.

options = {
    'sep': ', ',
    'end': ';\n'
}

print('value1', 'value2', **options)



"""Обзор операций со словарями"""

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# len(d) – количество элементов.
print(len(phonebook), 'entries found')

print()

# d[key] – получение значения с ключом key. Если такой ключ не существует
# и отображение реализует специальный метод __missing__(self, key), то он
# вызывается. Если ключ не существует и метод __missing__ не определён,
# выбрасывается исключение KeyError.
try:
    print('Mary:', phonebook['Mary'])
    print('Lumberjack:', phonebook['Lumberjack'])
except KeyError as e:
    print('No entry for', *e.args)

print()

# d[key] = value – изменить значение или создать новую пару ключ-значение, если
# ключ не существует.
phonebook['Lumberjack'] = '000-777'

# key in d, key not in d – проверка наличия ключа в отображении.
for person in ('Guido', 'Mary', 'Ahmed'):
    if person in phonebook:
        print(person, 'is in the phonebook')
    else:
        print('No entry found for', person)

print()

# iter(d) – то же самое, что iter(d.keys()).
print('People in the phonebook:')
for person in phonebook:
    print(person)

print()

# copy() – создать неполную копию словаря.
phonebook_copy = phonebook.copy()
print('Phonebook:', phonebook)
print('Phonebook copy:', phonebook_copy)

print()

# clear() – удалить все элементы словаря.
phonebook_copy.clear()
print('Phonebook:', phonebook)
print('Phonebook copy:', phonebook_copy)

print()

# (метод класса) dict.fromkeys(sequence[, value]) – создаёт новый словарь с
# ключами из последовательности sequence и заданным значением (по умолчанию –
# None).
numbers_dict = dict.fromkeys(range(3), 42)
print(numbers_dict)

print()

# d.get(key[, default]) – безопасное получение значения по ключу (никогда не
# выбрасывает KeyError).  Если ключ не найден, возвращается значение default
# (по-умолчанию – None).
for key in range(5):
    print('{}:'.format(key), numbers_dict.get(key, 0))

print()

# d.items() – в Python 3 возвращает объект представления словаря,
# соответствующий парам (двухэлементным кортежам) вида (ключ, значение).  В
# Python 2 возвращает соответствующий список, а метод iteritems() возвращает
# итератор.  Аналогичный метод в Python 2.7 – viewitems().
print('Items:', phonebook.items())

# d.keys() – в Python 3 возвращает объект представления словаря,
# соответствующий ключам словаря.  В Python 2 возвращает соответствующий
# список, а метод iterkeys() возвращает итератор.  Аналогичный метод в Python
# 2.7 – viewkeys().
print('Keys:', phonebook.keys())

# d.values() – в Python 3 возвращает объект представления словаря,
# соответствующий значениям.  В Python 2 возвращает соответствующий список, а
# метод itervalues() возвращает итератор.  Аналогичный метод в Python 2.7 –
# viewvalues().
print('Values:', phonebook.values())

print()

# d.pop(key[, default]) – если ключ key существует, удаляет элемент из словаря
# и возвращает его значение.  Если ключ не существует и задано значение
# default, возвращается данное значение, иначе выбрасывается исключение
# KeyError.
number = phonebook.pop('Lumberjack')
print('Deleted Lumberjack (was ' + number + ')')
print(phonebook)

print()

# d.popitem() – удаляет произвольную пару ключ-значение и возвращает её.  Если
# словарь пустой, возникает исключение KeyError.  Метод полезен для алгоритмов,
# которые обходят словарь, удаляя уже обработанные значения (например,
# определённые алгоритмы, связанные с теорией графов).
person = phonebook.popitem()
print('Popped {} (phone: {})'.format(*person))

print()

# d.setdefault(key[, default]) – если ключ key существует, возвращает
# соответствующее значение.  Иначе создаёт элемент с ключом key и значением
# default.  default по умолчанию равен None.
for person in ('Jack', 'Liz'):
    phone = phonebook.setdefault(person, '000-000')
    print('{}: {}'.format(person, phone))

print(phonebook)

print()

# d.update(mapping) – принимает либо другой словарь или отображение, либо
# итерабельный объект, состоящий из итерабельных объектов – пар ключ-значение,
# либо именованные аргументы.  Добавляет соответствующие элементы в словарь,
# перезаписывая элементы с существующими ключами.
phonebook.update({'Alex': '832-438', 'Alice': '231-987'})
phonebook.update([('Joe', '217-531'), ('James', '783-428')])
phonebook.update(Carl='783-923', Victoria='386-486')
print(phonebook)



"""Использование представлений словарей"""

# Объекты, возвращаемые методами items(), keys() и values() (viewitems(),
# viewkeys(), viewvalues() в Python 2.7) – это объекты представления словаря.
# Они предоставляют динамическое представление элементов словаря, то есть
# изменения данного словаря автоматически отображаются и на этих объектах.
#
# Операции с представлениями словарей:
# • iter(dictview) – получение итератора
#   по ключам, значениям или парам ключей и значений.  Все представления словарей
#   при итерировании возвращают элементы словаря в одинаковом порядке.  При
#   попытке изменить словарь во время итерирования может возникнуть исключение
#   RuntimeError.
# • len(dictview) – количество элементов в словаре.
# • x in dictview – проверка существования ключа, значения или пары ключ-значение
#   в словаре.

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# Итерирование
n = 0
for val in values:
    n += val
print(n)

# Ключи и значения итерируются в таком же порядке
print(list(keys))
print(list(values))

# Объекты представлений динамически отображают изменения в словаре
del dishes['eggs']
del dishes['sausage']
print(list(keys))

# Также они поддерживают операции с множествами
print(keys & {'eggs', 'bacon', 'salad'})
print(keys ^ {'sausage', 'juice'})



"""Пример использования collections.Counter"""

from collections import Counter

# collections.Counter -- это подкласс dict, предназначенный для подсчёта
# хешируемых объектов.  Также его иногда называют мультимножеством.  Элементы
# сохраняются как ключи словаря, а их количество -- как значения.

counter = Counter()
counter[1] += 1
for i in range(3):
    print(counter[i])

print()

c = Counter('abcdeabcdabcaba')  # подсчитать количество каждого символа в строке

print(c.most_common(3))         # три наиболее частых элемента
print(sorted(c))                # все уникальные элементы
print(sorted(c.elements()))     # все элементы

print(sum(c.values()))          # сумма значений

print(c['a'] )                  # количество букв 'a'

for elem in 'shazam':           # добавить новые буквы
    c[elem] += 1

print(c['a'])                   # теперь в счётчике семь букв 'a'
del c['b']                      # удалить все 'b'
print(c['b'])

d = Counter('simsalabim')       # создать новый счётчик
c.update(d)                     # добавить его элементы в первый
print(c['a'])                   # теперь в нём девять 'a'

c.clear()                       # очистить счётчик
print(c)

# внимание: если счёт элемента установить или уменьшить до нуля, он останется в
# счётчике, пока не будет удалён явно
c = Counter('aaabbc')
c['b'] -= 2
print(c.most_common())






