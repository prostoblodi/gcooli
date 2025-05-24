def check_age(age):
    assert age >= 18, \
        "Вам має бути 18 років або більше"
    print("Ви можете використовувати цей сервіс")

try:
    check_age(21)
    check_age(10)
except AssertionError as e:
    print(e)