def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(N, Z):
    if N > Z:
        N, Z = Z, N

    for num in range(N, Z + 1):
        if is_prime(num):
            yield num

import random


N = random.randint(1, 100)
Z = random.randint(N, 200)

print(f"Діапазон простих чисел від {N} до {Z}:")
prime_numbers = list(prime_generator(N, Z))
print(" ".join(map(str, prime_numbers)))