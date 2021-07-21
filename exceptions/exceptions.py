# All standard exception extends  Exception or BaseException
# User exception extends Exception
# to trow Exception use raise

# raise ValueError

# Exception handling

# try:
# except Exception1:

# except Exception2:

# except:

# else:

# finally:

# Firstly we define short then generic exception
# try:
# except (Exception3, Exception4):  # for 3 and 4
#    pass
# except Exception5 as exception:   # example of exeption acessible by name exception
#    pass
# except:
#    pass


# when run enter second value = 0
import warnings

print("calcukator")
try:
    a = float(input("a =  "))
    b = float(input("b =  "))
    print(a / b)
# except Exception as error:
#    print(type(error))
except ZeroDivisionError:
    print("you cannot divide by zero")

print("Stop the calculator")

# bad practice
try:
    3 / 0
except:
    pass
print("program flows")


class MyException(Exception):
    pass


try:
    raise MyException("error")
except MyException as e:
    print(e)
except Exception:
    print('some exception')


def divide_numbers():
    loop = True
    while loop:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            print('Result:', first_number / second_number)
            loop = False
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            print()
            loop = True


if __name__ == '__main__':
    divide_numbers()


# Distructor exception ignored and just print
class MyClass(object):
    def __del__(self):
        raise ZeroDivisionError


print('Creating object')
obj = MyClass()

print('Deleting object')
del obj

print('Done')

##### raise generate exception again
try:
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception:', error)
        raise
except ValueError:
    print('ValueError detected')

a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print("hi")
#    raise ValueError


#####
a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as error:
    #    raise ValueError('variable b is incorrect') from error
    pass
###
a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as error:
    #    raise ValueError('variable b is incorrect') from None
    pass


#### else
def divide_numbers():
    while True:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            result = first_number / second_number
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            print()
        else:
            print('Result:', result)
            break


if __name__ == '__main__':
    divide_numbers()


def function_that_may_fail():
    response = None
    while response != 'y' and response != 'n':
        response = input('Raise an exception? (y/n) ')
    if response == 'y':
        raise Exception


try:
    function_that_may_fail()
except:
    print('Exception handler')
finally:
    print('Finally block')

try:
    # 2 / 0
    2 / 1
finally:
    print('Finally block is always executed')

# warnings


def input_body_parameter(name, unit, supposed_maximum):
    parameter = float(input('Enter your {} (in {}): '.format(name, unit)))
    if parameter <= 0:
        raise ValueError(name + ' cannot be negative')
    if parameter > supposed_maximum:
        warnings.warn('suspiciously large value of ' + name)
    return parameter


def input_mass():
    return input_body_parameter(name='mass', unit='kg', supposed_maximum=100)


def input_height():
    return input_body_parameter(name='height', unit='m', supposed_maximum=2)


def calculate_bmi(mass, height):
    return mass / (height ** 2)


def main():
    mass = input_mass()
    height = input_height()
    bmi = calculate_bmi(mass, height)
    print('Your body mass index is', bmi)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""
Пример проверки реализации объектом необходимого интерфейса
с использованием стиля Look Before You Leap (не рекоммендуется).
"""


# Классы равнобедренных фигур

class IsoscelesShape(object):
    def __init__(self, side):
        self.side = side

    def render(self):
        print(self)
        self.draw()
        print()

    def __str__(self):
        return 'Abstract figure object'

    def draw(self):
        pass


class Square(IsoscelesShape):
    def draw(self):
        for _ in range(self.side):
            print('*' * self.side)

    def __str__(self):
        return 'Square with a side of {!r}'.format(self.side)


class IsoscelesRightTriangle(Square):
    def draw(self):
        for i in range(1, self.side + 1):
            print('*' * i)

    def __str__(self):
        return 'Isosceles right triangle with a side of {!r}'.format(self.side)


# Класс, который не наследуется от классов равнобедренных фигур
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self):
        print('Rectangle with sides {!r} and {!r}'.format(self.width, self.height))
        print('\n'.join(['*' * self.width] * self.height))
        print()


def main():
    shapes = [Square(5), IsoscelesRightTriangle(3), Rectangle(10, 3), 42]
    for shape in shapes:
        if hasattr(shape, 'render'):
            shape.render()
        else:
            print(repr(shape), 'is not a shape.')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""
Пример проверки реализации объектом необходимого интерфейса
с использованием стиля Easier to Ask for Forgiveness that Permission
(рекоммендуется).
"""


# Классы равнобедренных фигур

class IsoscelesShape(object):
    def __init__(self, side):
        self.side = side

    def render(self):
        print(self)
        self.draw()
        print()

    def __str__(self):
        return 'Abstract figure object'

    def draw(self):
        pass


class Square(IsoscelesShape):
    def draw(self):
        for _ in range(self.side):
            print('*' * self.side)

    def __str__(self):
        return 'Square with a side of {!r}'.format(self.side)


class IsoscelesRightTriangle(Square):
    def draw(self):
        for i in range(1, self.side + 1):
            print('*' * i)

    def __str__(self):
        return 'Isosceles right triangle with a side of {!r}'.format(self.side)


# Класс, который не наследуется от классов равнобедренных фигур
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self):
        print('Rectangle with sides {!r} and {!r}'.format(self.width, self.height))
        print('\n'.join(['*' * self.width] * self.height))
        print()


def main():
    shapes = [Square(5), IsoscelesRightTriangle(3), Rectangle(10, 3), 42]
    for shape in shapes:
        try:
            shape.render()
        except AttributeError:
            print(repr(shape), 'is not a shape.')


if __name__ == '__main__':
    main()
