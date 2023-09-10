
import random
numbers = [random.randint(1, 10) for _ in range(20)]
print("Повторюються числа:", [x for x in set(numbers) if numbers.count(x) > 1])

