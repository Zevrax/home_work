def longest_words(file):

    with open(file, 'r', encoding='utf-8') as f:

        words = f.read().split()


        max_length = 0


        longest_words_list = []


        for word in words:




            if len(word) > max_length:
                max_length = len(word)
                longest_words_list = [word]
            elif len(word) == max_length:
                longest_words_list.append(word)

        return longest_words_list


file_path = 'article.txt'


result = (longest_words(file_path))


if len(result) == 1:
    print(result[0])
else:
    print(result)