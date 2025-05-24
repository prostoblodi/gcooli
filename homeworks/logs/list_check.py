def process_list(input_list):
    assert len(input_list) >= 3, \
        "Список повинен містити принаймні 3 елементи"
    print(f"Список містить {len(input_list)} елементів")

try:
    process_list([1,2,3,4,5,6])
    process_list([1,2])
except AssertionError as e:
    print(e)