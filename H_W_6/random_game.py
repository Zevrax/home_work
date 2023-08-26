
string = input("Введіть рядок: ")


char = input("Введіть символ для пошуку: ")

found_indices = []


for i in range(len(string)):
    if string[i] == char:
        found_indices.append(i)

if len(found_indices) > 0:
    print(f"Символ '{char}' знайдений у рядку на позиціях: {', '.join(map(str, found_indices))}")
else:
    print(f"Символ '{char}' не знайдений у рядку.")