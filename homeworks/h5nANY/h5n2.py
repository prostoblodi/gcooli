to_convert = input("Введіть число, для того щоб ми його конвертували в ціле - ")
try:
    print("Результат -",int(to_convert))
except ValueError:
    print("Це не число.")