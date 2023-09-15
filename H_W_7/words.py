
sentence = input("Введіть речення, в якому більше двох слів: ")


words_list = sentence.split(" ")


words_list = [word for word in words_list if word]


words_list.sort()


print("Індекс | Слово")
print("-" * 20)
for index, word in enumerate(words_list):
    print(f"{index + 1:^7} | {word}")


word_count = len(words_list)
print(f"Кількість слів: {word_count}")