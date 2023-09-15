import random

print("Привіт! Загадайте число від 0 до 100.")
lower_bound = 0
upper_bound = 100
steps = 0

while True:
    guess = random.randint(lower_bound, upper_bound)
    response = input(f"Чи є ваше число {guess}? (більше/менше/так): ")

    if response == "більше":
        lower_bound = guess + 1
        steps += 1
    elif response == "менше":
        upper_bound = guess - 1
        steps += 1
    elif response == "так":
        steps += 1
        print(f"Програма вгадала ваше число {guess} за {steps} кроків!")
        break
    else:
        print("Будь ласка, введіть 'більше', 'менше' або 'так'.")