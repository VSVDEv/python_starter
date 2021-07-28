"""Пример использования функции map"""

string = '2 4 8 15 42'
numbers = map(int, string.split())
print(list(numbers))

"""Пример использования функции filter"""

numbers = [3, 2, -1, 0, 15, -8, -7, 3, -3, 8]
positive_numbers = filter(lambda x: x > 0, numbers)
print(list(positive_numbers))

"""Пример использования функции reduce"""

from functools import reduce

numbers = [3, 2, 1, 8, -3, -2]
# Произведение всех чисел списка
product = reduce(lambda x, y: x * y, numbers)

print(product)

"""Пример использования функции lru_cache модуля functools"""

from functools import lru_cache


# Здесь функция вычисления чисел Фибоначчи записана рекурсивно, но по
# произоводительности и расходу памяти она будет сравнима с нерекурсивной
@lru_cache(maxsize=None)
def fibonacci(index):
    if index < 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


for i in range(1, 1000):
    print(fibonacci(i))

"""Пример использования функции partial модуля functools"""

from functools import partial

# Частичное применение функции
print_with_comma = partial(print, sep=', ')

print_with_comma(2, 3, 5)

"""Пример использования комбинаторных генераторов модуля itertools"""

from itertools import permutations, combinations, combinations_with_replacement

print(list(permutations('ABC', 2)))
print()

print(list(combinations('ABC', 2)))
print()

print(list(combinations_with_replacement('ABC', 2)))

"""Пример использования функции product модуля itertools"""

from itertools import product

for a, b in product(range(2), range(3)):
    print(a, b)

"""Пример использования функции chain модуля itertools"""

from itertools import chain

for i in chain(range(2), range(3)):
    print(i)

"""Пример использования функций takewhile и dropwhile модуля itertools"""

from itertools import takewhile, dropwhile

numbers = [1, 4, 6, 4, 1]
predicate = lambda x: x < 5

for value in takewhile(predicate, numbers):
    print(value)

print()

for value in dropwhile(predicate, numbers):
    print(value)

"""Пример использования модуля operator"""

from operator import neg, mul, le
from functools import reduce, partial

# Сделать числа списка отрицательными
print(list(map(neg, [2, 4, 8, 9, 1])))

# Вычислить произведение элементов списка
print(reduce(mul, [3, 4, 5]))

# Оставить только числа, большие или равные пяти (используется оператор <=, так
# как при помощи функции partial применяется первый аргумент, то есть условие
# выглядит как 5 <= x).
print(list(filter(partial(le, 5), [5, 4, 8, 1, 3, 10])))
