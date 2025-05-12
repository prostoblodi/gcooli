file_path = input("Введіть шлях до файлу: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Вміст файлу: \n{content}")
except FileNotFoundError:
    print("Цього файлу не існує.")

