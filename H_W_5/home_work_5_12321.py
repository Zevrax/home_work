num = int(input("введіть число від 3 до 9"))
n = []

if num < 10 or num > 3:
    for i in range(1, num + 1):
        for j in range(1, num + 1 - i):
            print(' ', end='')

        for j in range(1, i + 1):
            print(j, end='')

        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()

else:
    print("не в діапазоні")

