import some_library

try:
    some_library.some_function()
    some_library.notexisting_function()
except AttributeError:
    print("Функція не знайдена")