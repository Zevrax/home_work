with open('output.txt', 'w', encoding='utf-8') as file:
    while True:

        input_text = input("Введіть рядок (для завершення введення натисніть Enter без тексту): ")


        if not input_text:
            break


        file.write('\n' + input_text)

print("Введення завершено. Дані записано у файл 'output.txt'.")