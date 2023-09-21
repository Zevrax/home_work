import re

def password_requirements(prompt):
    while True:
        password = input(prompt)

        
        if not password or any(char.isspace() for char in password):
            print("Пароль не може бути пустим і не повинен містити пробільних символів.")
            continue


        if len(password) < 8:
            print("Пароль повинен мати щонайменше 8 символів.")
            continue


        if not (re.search(r'\d', password) and re.search(r'[a-zA-Z]', password) and re.search(r'[!@#$%^&*]', password)):
            print("Пароль повинен містити щонайменше 1 цифру, 1 букву та 1 спеціальний символ (!@#$%^&*).")
            continue

        return password

def password_decorator(func):
    def wrapper():
        print("Потрібно створити пароль, який відповідає наступним вимогам:")
        print("- Пароль не може бути пустим і не повинен містити пробільних символів.")
        print("- Пароль повинен мати щонайменше 8 символів.")
        print("- Пароль повинен містити щонайменше 1 цифру, 1 букву та 1 спеціальний символ (!@#$%^&*).")

        while True:
            password = func()
            if password is None:
                continue
            print("Пароль відповідає вимогам.")
            return password

    return wrapper

@password_decorator
def get_password():
    return password_requirements("Будь ласка, введіть пароль: ")

if __name__ == "__main__":
    password = get_password()
    print("Ваш пароль:", password)