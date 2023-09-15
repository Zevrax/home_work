def dict_handler(link_on_dict, key, default_value=None):
    try:
        if key not in link_on_dict:
            link_on_dict[key] = default_value
        return link_on_dict[key]
    except TypeError:
        raise Exception("Помилка: ключ не може бути змінюваним типом даних.")
    finally:
        print("Операція завершена.")

# Приклад використання:
my_dict = {"name": "John"}
key = "age"
default_value = 25
result = dict_handler(my_dict, key, default_value)
print("Значення ключа", key, ":", result)