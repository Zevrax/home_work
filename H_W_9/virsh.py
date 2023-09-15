import string

text = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.
Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами."""


translator = str.maketrans("", "", string.punctuation)
cleaned_text = text.translate(translator)


words = cleaned_text.lower().split()


word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


most_common_word = max(word_count, key=word_count.get)
least_common_word = min(word_count, key=word_count.get)


print(f"Найбільше входження: Слово '{most_common_word}' зустрічається {word_count[most_common_word]} раз(ів).")
print(f"Найменше входження: Слово '{least_common_word}' зустрічається {word_count[least_common_word]} раз(ів).")