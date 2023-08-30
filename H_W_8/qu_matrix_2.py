import random

def generate_random_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.randint(1, 100)) 
        matrix.append(row)
    return matrix

N = int(input("Введіть розмір матриці N: "))
matrix = generate_random_matrix(N)

for row in matrix:
    print(row)


diagonal_sum = sum(matrix[i][i] for i in range(N))
print("Сума чисел по діагоналі:", diagonal_sum)


last_column_sum = sum(matrix[i][-1] for i in range(N))
print("Сума чисел останнього стовбця:", last_column_sum)