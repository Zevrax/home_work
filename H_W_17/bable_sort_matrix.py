import random


def input_matrix_size():
    while True:
        try:
            M = int(input("Введіть розмір матриці M (більше 5): "))
            if M > 5:
                return M
            else:
                print("Розмір матриці повинен бути більше 5.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")


def create_matrix(M):
    matrix = []
    for _ in range(M):
        row = [random.randint(1, 100) for _ in range(M)]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    M = len(matrix)
    sums = [0] * M

    for i in range(M):
        for j in range(M):
            sums[j] += matrix[i][j]
            print(matrix[i][j], end='\t')
        print()

    for col_sum in reversed(sums):
        print(col_sum, end='\t')
    print("\n")


def bubble_sort(column, reverse=False):
    n = len(column)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if reverse:
                if column[j] < column[j + 1]:
                    column[j], column[j + 1] = column[j + 1], column[j]
            else:
                if column[j] > column[j + 1]:
                    column[j], column[j + 1] = column[j + 1], column[j]


def sort_matrix(matrix):
    sums = [sum(column) for column in zip(*matrix)]
    sorted_columns = [list(column) for column in zip(*matrix)]

    bubble_sort(sums)

    for i in range(len(sorted_columns)):
        if i % 2 == 0:
            bubble_sort(sorted_columns[i], reverse=True)  
        else:
            bubble_sort(sorted_columns[i])

    sorted_matrix = [list(column) for column in zip(*sorted_columns)]
    return sorted_matrix


def main():
    M = input_matrix_size()
    matrix = create_matrix(M)

    print("\nВихідна матриця:")
    print_matrix(matrix)

    sorted_matrix = sort_matrix(matrix)

    print("\nВідсортована матриця:")
    print_matrix(sorted_matrix)


if __name__ == "__main__":
    main()