
sentence = input("Введіть речення з більше ніж 2-ма словами: ")


words_list = sentence.split(" ")


words_list = [word for word in words_list if word != ""]


sorted_words_list = sorted(words_list)


for index, word in enumerate(sorted_words_list):
    print(f"{index + 1}: {word}")


print("Кількість слів:", len(sorted_words_list))