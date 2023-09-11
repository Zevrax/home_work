from mcolour import custom_style


def print_poem_fragment():
    poem_fragment = """
    В гаї та в лісі, під вербою села,
    Де співав соловей у весняну пору,
    Зустрілись кохані два молоденьких дола,
    І губами губи в ніжності губили.
    """

    # Редагуємо один рядок фоном
    edited_line1 = "    Де співав соловей у весняну пору,"



    styled_poem = ""
    for line in poem_fragment.split('\n'):
        words = line.split()
        for i in range(len(words)):
            # Надаємо стиль Bold словам з трьох символів
            if len(words[i]) == 3:
                words[i] = custom_style(words[i], style="1m")  # 1m - стиль Bold

        # Встановлюємо фон для рядків
        if line == edited_line1:
            styled_line = custom_style(line, style="3m", text_color="30m", background_color="41m")

        else:
            styled_line = ' '.join(words)

        styled_poem += styled_line + '\n'

    print(styled_poem)


if __name__ == "__main__":
    print_poem_fragment()