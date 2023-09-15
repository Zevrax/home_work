import random

n_1, n_2 = [random.randint(1, 100) for _ in range(10)], [random.randint(1, 100) for _ in range(10)]

print("Кількість різних чисел, що містяться в обох списках одночасно:", len(set(n_1) & set(n_2)))