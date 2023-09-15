input_string = 'python is good language to code'


input_string = input_string.replace(' ', '')


letter_count = {}
for letter in input_string:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1


print(letter_count)