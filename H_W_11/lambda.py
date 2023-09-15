
power_function = lambda x, y=2: x ** y


x = int(input("Введіть число x: "))
y = int(input("Введіть ступінь y (за замовчуванням 2): "))


result = list(map(lambda x: power_function(x, y), [x]))
print("Результат:", result)