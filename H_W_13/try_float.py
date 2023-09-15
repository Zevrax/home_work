def process_values():
    value1 = input("Введіть перше значення: ")
    value2 = input("Введіть друге значення: ")

    try:
        result = float(value1) + float(value2)
    except ValueError:
        result = value1 + value2

    return result


result = process_values()
print("Результат:", result)