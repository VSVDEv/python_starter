"""Пример работы с функциями как с объектами первого класса"""

# Создание ссылки на объект
out = print
out('Hello')


# Сохранение ссылок на функции в структуре данных

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


operations = {
    '+': add,
    '-': sub
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

"""Пример использования лямбда-выражений"""

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

"""Пример замыкания"""


def make_closure():
    variable = 42

    def closure():
        return variable

    return closure


fn = make_closure()
print(fn())

"""Демонстрация часто допускаемой ошибки и способа её решения"""


def make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1
    (неправильная реализация)
    """

    functions = []

    for i in range(1, n + 1):
        functions.append(lambda x: x ** i)

    return functions


for function in make_powers(3):
    print(function(2))

# Видно, что результататом было не 2, 4, 8, как можно было бы ожидать,
# а 8, 8, 8

print()


# Причиной этого является так называемое позднее связываение.  К тому моменту,
# когда вызываются функции из списка, цикл в функции make_powers уже выполнен и
# переменная i всегда равна n + 1.

# Для того, чтобы избавиться от этого, необходимо скопировать данную переменную
# в локальные переменные каждой функции.  Единственный способ создать локальную
# переменную в лямбда-выражении -- это создать параметр функции.

def make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1
    (правильная реализация)
    """

    functions = []

    for i in range(1, n + 1):
        functions.append(lambda x, i=i: x ** i)

    return functions


for function in make_powers(3):
    print(function(2))

"""Пример каррирования функции"""


def ordinary_add(x, y):
    """Обычная функция"""
    return x + y


def curryied_add(x):
    """Каррированная функция"""

    def do_add(y):
        return x + y

    return do_add


print(ordinary_add(2, 3))
print(curryied_add(2)(3))

# Каррирование делает лёгким частичное применение функций
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))

print()

# В виде лямбда-выражений
ordinary_add = lambda x, y: x + y
curryied_add = lambda x: lambda y: x + y

print(ordinary_add(2, 3))
print(curryied_add(2)(3))
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))

"""Пример создания декоратора"""


def decorator(fn):
    """Пример декоратора"""

    def decorated_fn(*args, **kwargs):
        """Модифицированная функция"""

        print('Decorated function says:')
        fn(*args, **kwargs)  # вызов изначальной функции
        print()

    return decorated_fn


@decorator
def hello():
    print('Hello!')


# Вызов декорированной функции
hello()


def cast_result(type_):
    """Пример создания декоратора с параметром"""

    def cast_decorator(function):
        """Сам декоратор"""

        def decorated_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return type_(result)

        return decorated_function

    return cast_decorator


@cast_result(float)
def add(x, y):
    return x + y


print(add(2, 3))

import decimal


@cast_result(repr)
@cast_result(decimal.Decimal)
def div(x, y):
    return x / y


print(div(3, 2))
