import random

def generate_chessboard():
    # Розмір дошки (зазвичай 8x8 для шахів)
    board_size = 8

    # Шахова дошка
    chessboard = []

    # Список фігур
    pieces = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖",
              "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"]

    # Випадковий вибір кольорів для фігур та полів
    piece_color = random.choice(["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m"])
    empty_color = random.choice(["\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m"])

    for i in range(board_size):
        row = []
        for j in range(board_size):
            # Визначаємо колір для клітинки
            cell_color = piece_color if (i + j) % 2 == 0 else empty_color

            # Випадково вибираємо фігуру або порожнє поле
            piece = random.choice(pieces) if random.randint(0, 1) == 1 else " "
            row.append(cell_color + piece + "\033[0m")
        chessboard.append(row)

    return chessboard

def print_chessboard(chessboard):
    # Виведення шахової дошки
    for row in chessboard:
        print(" ".join(row))

if __name__ == "__main__":
    chessboard = generate_chessboard()
    print_chessboard(chessboard)