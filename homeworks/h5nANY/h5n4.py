import some_libary

try:
    some_libary.some_function()
    some_libary.notexisting_function()
except AttributeError:
    print("Функція не знайдена")