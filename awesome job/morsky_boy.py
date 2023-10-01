import random

# Розмір ігрового поля
field_size = 10

# Символи для псевдографіки
empty_cell = ' '
ship_cell = 'O'
miss_cell = 'X'
hit_cell = '*'


# Функція для створення пустого ігрового поля
def create_empty_field():
    return [[empty_cell] * field_size for _ in range(field_size)]


# Функція для виведення ігрового поля на екран
def print_field(player_field, computer_field):
    print("Поле гравця:")
    print("   0 1 2 3 4 5 6 7 8 9")
    for i, row in enumerate(player_field):
        print(f"{i}  {' '.join(row)}")
    print("\nПоле комп'ютера:")
    print("   0 1 2 3 4 5 6 7 8 9")
    for i, row in enumerate(computer_field):
        print(f"{i}  {' '.join(row)}")
    print()


# Функція для розміщення корабля на ігровому полі
def place_ship(field, ship_size):
    while True:
        try:
            print_field(player_field, computer_field)
            print(f"Розмістіть корабель розміром {ship_size}")
            x = int(input("Введіть рядок (0-9): "))
            y = int(input("Введіть стовпчик (0-9): "))
            orientation = input("Введіть орієнтацію (горизонтально - 'h', вертикально - 'v'): ").lower()

            if orientation == 'h':
                if y + ship_size > field_size:
                    raise ValueError("Корабель не вміщається на полі")
                for i in range(y, y + ship_size):
                    if field[x][i] == ship_cell:
                        raise ValueError("Корабель перекриває інший корабель")
            elif orientation == 'v':
                if x + ship_size > field_size:
                    raise ValueError("Корабель не вміщається на полі")
                for i in range(x, x + ship_size):
                    if field[i][y] == ship_cell:
                        raise ValueError("Корабель перекриває інший корабель")
            else:
                raise ValueError("Некоректний ввід. Введіть 'h' або 'v' для орієнтації корабля")

            for i in range(ship_size):
                if orientation == 'h':
                    field[x][y + i] = ship_cell
                else:
                    field[x + i][y] = ship_cell
            break
        except (ValueError, IndexError):
            print("Некоректні координати або неможливо розмістити корабель. Повторіть спробу.")


# Функція для випадкового розміщення кораблів
def place_random_ships(field):
    ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # Розміри кораблів
    for ship_size in ship_sizes:
        while True:
            x = random.randint(0, field_size - 1)
            y = random.randint(0, field_size - 1)
            orientation = random.choice(['h', 'v'])
            try:
                if orientation == 'h':
                    if y + ship_size > field_size:
                        raise ValueError
                    for i in range(y, y + ship_size):
                        if field[x][i] != empty_cell:
                            raise ValueError
                elif orientation == 'v':
                    if x + ship_size > field_size:
                        raise ValueError
                    for i in range(x, x + ship_size):
                        if field[i][y] != empty_cell:
                            raise ValueError
                for i in range(ship_size):
                    if orientation == 'h':
                        field[x][y + i] = ship_cell
                    else:
                        field[x + i][y] = ship_cell
                break
            except (ValueError, IndexError):
                continue


# Функція для ходу гравця
def player_turn(player_field, computer_field):
    while True:
        try:
            print_field(player_field, computer_field)
            x = int(input("Введіть рядок (0-9): "))
            y = int(input("Введіть стовпчик (0-9): "))
            if computer_field[x][y] == empty_cell:
                return x, y
            else:
                print("Цю клітину ви вже стріляли.")
        except (ValueError, IndexError):
            print("Некоректні координати. Повторіть спробу.")


# Функція для ходу комп'ютера (з випадковим вибором координат)
def computer_turn(player_field, computer_field):
    while True:
        x = random.randint(0, field_size - 1)
        y = random.randint(0, field_size - 1)
        if player_field[x][y] == empty_cell:
            return x, y


# Функція для перевірки, чи закінчилася гра (всі кораблі знищені)
def is_game_over(field):
    return all(cell != ship_cell for row in field for cell in row)


# Основна функція гри
def play_game():
    print("Гра Морський бій")

    # Створення ігрових полів для гравця і комп'ютера
    player_field = create_empty_field()
    computer_field = create_empty_field()

    print("Виберіть режим розміщення кораблів:")
    print("1. Ручне розміщення")
    print("2. Автоматичне розміщення")

    while True:
        choice = input("Ваш вибір (1 або 2): ")
        if choice == '1':
            print("Ручне розміщення кораблів:")
            for ship_size in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
                place_ship(player_field, ship_size)
            place_random_ships(computer_field)
            break
        elif choice == '2':
            print("Автоматичне розміщення кораблів комп'ютером:")
            place_random_ships(player_field)
            place_random_ships(computer_field)
            break
        else:
            print("Некоректний вибір. Виберіть 1 або 2.")

    player_score = 0
    computer_score = 0

    while True:
        # Хід гравця
        print("Ваш хід:")
        x, y = player_turn(player_field, computer_field)
        if computer_field[x][y] == ship_cell:
            print("Ви попали!")
            computer_field[x][y] = hit_cell
            player_score += 1
        else:
            print("Ви промахнулися.")
            computer_field[x][y] = miss_cell

        if is_game_over(computer_field):
            print("Гра завершена. Ви виграли!")
            break

        # Хід комп'ютера
        print("Хід комп'ютера:")
        x, y = computer_turn(player_field, computer_field)
        if player_field[x][y] == ship_cell:
            print("Комп'ютер попав!")
            player_field[x][y] = hit_cell
            computer_score += 1
        else:
            print("Комп'ютер промахнувся.")
            player_field[x][y] = miss_cell

        if is_game_over(player_field):
            print("Гра завершена. Комп'ютер виграв!")
            break


if __name__ == "__main__":
    play_game()
