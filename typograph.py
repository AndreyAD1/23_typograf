import re
import regex


# замена кавычек ' и " на « »
# в нужных местах заменить дефисы на тире
# замена дефисов на короткое тире в номерах телефонов
# связывание чисел с последующими словами неразрывным пробелом
# удаление лишних пробелов и переносов строк
# связывание союзов и любых слов из 1-2 символов с последующими словами


def get_text():
    return '''
    - Что ты говоришь? Рим - столица Италии. Человек-пароход. Звоните: 228-36-956 -6 Петя-1 2018 год 19   лет
    Falcon-9 совершил свой первый полёт.
    
    \n
    end
    start
    '''


def fix_left_quotes(string):
    left_quote_pattern = r'[\'|"](?=\w)'
    html_code_of_left_quote = '&#171'
    fixed_left_quotes = re.sub(
        left_quote_pattern,
        html_code_of_left_quote,
        string
    )
    return fixed_left_quotes


def fix_right_quotes(string):
    right_quote_pattern = r'(?<=\w)[\'|"]'
    html_code_of_right_quote = '&#187'
    fixed_right_quotes = re.sub(
        right_quote_pattern,
        html_code_of_right_quote,
        string
    )
    return fixed_right_quotes


def substitute_hyphens_for_dashes(string):
    dash_pattern = r'(?<=\s)-|-(?=\s)'
    dash_html_code = '&#8211'
    fixed_dashes = re.sub(dash_pattern, dash_html_code, string)
    return fixed_dashes


def substitute_hyphens_for_short_dashes(string):
    short_dash_pattern = r'(?<=\d)-(?=\d)'
    html_code_of_short_dash = '&#8211'
    fixed_short_dashes = re.sub(
        short_dash_pattern,
        html_code_of_short_dash,
        string
    )
    return fixed_short_dashes


def get_nonbreaking_space(match):
    if match.group(1) == ' ':
        str_without_end_space = match.group(0).rstrip()
        nonbreaking_space = '&#160'
        str_with_nonbreaking_space = str_without_end_space + nonbreaking_space
        return str_with_nonbreaking_space
    return match.group(0)


def add_nonbreaking_spaces(string):
    # TODO No nonbreaking space should be between 'Петя-1' and '2018'
    # search_pattern = r'(?<=[0-9])\s(?=\p{L})'
    # html_code_of_nonbreaking_space = '&#160'
    search_pattern = r'(\D)(\d+)(\s)(?=\p{L})'
    # match_object = regex.search(search_pattern, string)
    # get_nonbreaking_space(match_object)
    # html_code_of_nonbreaking_space = '!'
    text_with_nonbreaking_spaces = regex.sub(
        search_pattern,
        get_nonbreaking_space,
        string
    )
    return text_with_nonbreaking_spaces


def delete_redundant_spaces(string):
    redundant_space_pattern = r'[ \t\r\f\b][ \t\r\f\b]+'
    text_without_redundant_spaces = re.sub(
        redundant_space_pattern,
        ' ',
        string
    )
    return text_without_redundant_spaces


def delete_empty_lines(string):
    empty_line_pattern = r'\n\n+'
    text_without_empty_lines = re.sub(
        empty_line_pattern,
        '!',
        string
    )
    return text_without_empty_lines


if __name__ == '__main__':
    text = get_text()
    text = add_nonbreaking_spaces(text)
    text = fix_left_quotes(text)
    text = fix_right_quotes(text)
    text = substitute_hyphens_for_dashes(text)
    text = substitute_hyphens_for_short_dashes(text)
    text = delete_redundant_spaces(text)
    # text = delete_empty_lines(text)
    print(text)