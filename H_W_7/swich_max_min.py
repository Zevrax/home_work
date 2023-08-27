
input_list = input("Введіть список цілих чисел: ")
numbers = list(map(int, input_list.split()))


min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))


numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]


output = " ".join(map(str, numbers))
print("Вихідні дані:\n" + output)