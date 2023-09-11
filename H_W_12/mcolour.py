
colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m'
}

# Функція для надання кольору тексту
def color_text(text, colour_name):
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt


# Функція для надання стилів тексту (за замовчуванням - курсив)
def styled(text, code="3m"):
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt

# Функція для створення повідомлення про помилку з червоним текстом
def error_message(message):
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message

# Функція для створення попереджувального повідомлення з жовтим текстом
def warning_message(message):
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message

# Функція для створення інформаційного повідомлення з фіолетовим текстом
def info_message(message):
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message


def custom_style(text, style="0", text_color=None, background_color=None):
    style_code = f"\033[{style}" if style != "0" else ""  # Встановлюємо стиль (за замовчуванням - без стилю)
    text_color_code = f"\033[{text_color}" if text_color else ""  # Встановлюємо колір тексту
    background_color_code = f"\033[{background_color}" if background_color else ""  # Встановлюємо колір фону
    reset_code = "\033[0m"  # Збираємо код для скидання налаштувань до значень за замовчуванням
    styled_text = f"{style_code}{text_color_code}{background_color_code}{text}{reset_code}"
    return styled_text



"""
Example:
s = "\033[3m"
c = "\033[33m"
f  = "\033[41m";
clean = "\033[0m"
pattern = f"{s}{c}{f}{txt}{clean}"
"""



if __name__ == "__main__":
    print(warning_message("ups i did sit again"))
    print(error_message("wrong way"))
    print(info_message("thanks for info"))
