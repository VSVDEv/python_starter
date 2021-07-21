"""
Генераторы во многих случаях позволяют просто и удобно создавать итераторы.

Функция-генератор (generator function) – это функция, которая возвращает
специальный итератор-генератор (generator iterator)  (также объект-генератор –
generator object). Она характеризуется наличием ключевого слова yield
внутри функции.

Термин генератор (generator), в зависимости от контекста, может означать
либо функцию-генератор, либо итератор-генератор (чаще всего, последнее).

Методы __iter__ и __next__ у генераторов создаются автоматически.

Этот пример является модифицированным примером 05-iterator.py, в котором
вместо явного описания итератора используется генератор.
"""
# yield - stop function and give current value

def my_range(first, second=None, step=1):
    """Функция-генератор, работающая подобно стандартному классу range"""

    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    if step == 0:
        raise ValueError('step must not be zero')

    while (step > 0 and current < end) or (step < 0 and current > end):
        # yield выдаёт текущее значение и приостанавливает работу генератора.
        # При следующем вызове next выполнение продолжится с этого места.
        yield current
        current += step


def test_iterator():
    """Функция тестирования итератора"""

    radius = 30

    try:
        for start in range(-radius, radius + 1):
            for end in range(-radius, radius + 1):
                for step in range(-radius, radius + 1):
                    if step == 0:
                        continue

                    gen_range = my_range(start, end, step)
                    std_range = range(start, end, step)

                    # Получение списков значений
                    gen_range_values = list(gen_range)
                    std_range_values = list(std_range)

                    assert gen_range_values == std_range_values
    except AssertionError:
        print('Test failed')
        print('start =', start)
        print('end =', end)
        print('step =', step)
        print('gen_range_values =', gen_range_values)
        print('std_range_values =', std_range_values)
        print()
    else:
        print('iter tests passed normally')


def main():
    # Простая проверка генератора
    for i in my_range(10):
        print(i)

    print()

    # Использование генератора напрямую
    generator = my_range(2, 8, 2)
    try:
        while True:
            print(next(generator))
    except StopIteration:
        print()

    # Тестирование генератора
    test_iterator()


if __name__ == '__main__':
    main()



"""
При помощи генераторов можно описывать довольно широкий класс задач.
Одним из простых примеров является генерация последовательности
чисел Фибоначчи.

Последовательностью Фибоначчи называется такая последовательность
чисел, в которой первые два члена последовательности равны единице,
а все последующие -- сумме двух предыдущих.

Эта последовательность применяется, например, при прогнозировании
цен на товарных, фондовых и валютных биржах.
"""


def fibonacci(max_count):
    """Генерация max_count чисел Фибоначчи"""
    count = 0
    first, second = 0, 1

    while count < max_count:
        count += 1
        yield second
        first, second = second, first + second


def main():
    # Вывод 15 первых чисел Фибоначчи
    for number in fibonacci(15):
        print(number)


if __name__ == '__main__':
    main()


"""
Некоторые простые генераторы могут быть записаны в виде выражения.
Они выглядят как выражение, содержащее некоторые переменные, после
которого одно или несколько ключевых слов for, задающих, какие значения
должны принимать данные переменные (синтаксис соответствует заголовку
    цикла for), и ноль или несколько условий, фильтрующих генерируемые
значения (синтаксис соответствует заголовку оператора if). Такие выражения
называются выражениями-генераторами (generator expressions).
"""

generator = (x ** 2 + y for x in range(2, 7) for y in range(3) if x != 6)
for number in generator:
    print(number)

print()

print(sum(2 * x for x in range(5)))



"""
В Python 3 существуют так называемые подгенераторы (subgenerators).
Если в функции-генераторе встречается пара ключевых слов yield from,
после которых следует объект-генератор, то данный генератор делегирует
доступ к подгенератору, пока он не завершится (не закончатся его значения),
после чего продолжает своё исполнение.
"""

def generator():
    yield from (3 * x for x in range(5))
    yield from (2 * x for x in range(5, 10))


for i in generator():
    print(i)


"""
Сопрограмма (англ. coroutine) — компонент программы, обобщающий понятие
подпрограммы, который дополнительно поддерживает множество входных точек
(а не одну, как подпрограмма) и остановку и продолжение выполнения с
сохранением определённого положения.

Здесь показан пример такого шаблона использования сопрограмм, как
consumer-producer.
"""


import time
import random


def sleep(seconds):
    """Сопрограмма, которая приостанавливает сопрограмму,
    из которой была вызвана, на заданное количество секунд"""

    initial_time = time.time()
    while time.time() - initial_time < seconds:
        yield


def gen_data():
    """Функция генерации данных (например, показания с какого-то датчика)"""

    return random.randint(0, 100)


def consume():
    """Сопрограмма обработки данных"""

    running_sum = 0
    count = 0

    while True:
        data = yield
        running_sum += data
        count += 1
        print('Got data: {}\nTotal count: {}\nAverage: {}\n'.format(
            data, count, running_sum / count))


def produce(consumer):
    """Сопрограмма выдачи данных"""

    while True:
        yield from sleep(0.5)
        data = gen_data()
        consumer.send(data)
        yield


def main():
    # Создание обработчика данных
    consumer = consume()
    # Запуск сопрограммы
    consumer.send(None)

    # Создание производителя данных
    producer = produce(consumer)

    # Цикл событий (event loop)
    while True:
        next(producer)


if __name__ == '__main__':
    main()