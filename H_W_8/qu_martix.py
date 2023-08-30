def generate_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if i % 2 == 0:
                row.append(i)
            else:
                row.append(-(j + 1))
        matrix.append(row)
    return matrix

N = int(input("Введіть розмір матриці: "))
matrix = generate_matrix(N)

for row in matrix:
    print(row)