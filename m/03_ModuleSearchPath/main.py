"""Пример использования sys.path

При импортировании модулей интерпретатор Python ищет их в директориях и архивах,
список которых доступен как для чтения, так и для модификации в виде переменной
path встроенного модуля sys.
"""

import sys      # встроенный модуль sys
import os.path  # функции для работы с путями в файловой системе

print(sys.path)  # вывод списка путей поиска модулей

# Получение имени директории текущего модуля.
# __file__ -- путь к файлу текущего модуля
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_path = os.path.dirname(current_dir)

# Получение пути к первому примеру
example_00_path = os.path.join(os.path.dirname(parent_path), '00_Module')

# Добавление к пути поиска модулей
sys.path.append(example_00_path)

# Импортирование модуля fibonacci

import fibonacci

# Вызов его функции
print(fibonacci.nth_fibonacci(20))
