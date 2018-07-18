import re


# замена кавычек ' и " на « »
# в нужных местах заменить дефисы на тире
# замена дефисов на короткое тире в номерах телефонов
# связывание чисел с последующими словами неразрывным пробелом
# удаление лишних пробелов и переносов строк
# связывание союзов и любых слов из 1-2 символов с последующими словами


def get_text():
    return '\'Привет", Маша. Как "дела"?'


def fix_left_quotes(string):
    left_quote_pattern = r'[\'|"](?=\w)'
    html_code_of_left_quote = '&#171'
    fixed_left_quotes = re.sub(left_quote_pattern, html_code_of_left_quote, string)
    return fixed_left_quotes


def fix_right_quotes(string):
    right_quote_pattern = r'(?<=\w)[\'|"]'
    html_code_of_right_quote = '&#187'
    fixed_right_quotes = re.sub(right_quote_pattern, html_code_of_right_quote, string)
    return fixed_right_quotes


if __name__ == '__main__':
    text = get_text()
    text = fix_left_quotes(text)
    text = fix_right_quotes(text)
    print(text)