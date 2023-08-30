import random

numbers = [random.randint(1, 100) for _ in range(15)]  # Ви можете змінити кількість та діапазон випадкових чисел

odd_sum = sum(num for num in numbers if num % 2 != 0)
even_sum = sum(num for num in numbers if num % 2 == 0)

print("Список випадкових чисел:", numbers)
print("Сума непарних чисел:", odd_sum)
print("Сума парних чисел:", even_sum)

if odd_sum > even_sum:
    print("Так")
else:
    print("Ні")