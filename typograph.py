import regex


def get_text():
    return '''
    <p>- Что ты говоришь?</p> Рим - столица Италии. Человек-пароход. Звоните: 228-36-956 -6 Петя-1 2018 год 19   лет
    <b>Falcon-9</b> совершил свой первый полёт и он был успешен.\n2020 год
    2019 год.
    
    в 1989 году
    не очень-то круто
    '''


def fix_left_quotes(string):
    left_quote_pattern = r'[\'|"](?=\w)'
    html_code_of_left_quote = '&#171'
    fixed_left_quotes = regex.sub(
        left_quote_pattern,
        html_code_of_left_quote,
        string
    )
    return fixed_left_quotes


def fix_right_quotes(string):
    right_quote_pattern = r'(?<=\w)[\'|"]'
    html_code_of_right_quote = '&#187'
    fixed_right_quotes = regex.sub(
        right_quote_pattern,
        html_code_of_right_quote,
        string
    )
    return fixed_right_quotes


def substitute_hyphens_for_dashes(string):
    dash_pattern = r'(?<=\s)-|-(?=\s)'
    dash_html_code = '&#8211'
    fixed_dashes = regex.sub(dash_pattern, dash_html_code, string)
    return fixed_dashes


def substitute_hyphens_for_short_dashes(string):
    short_dash_pattern = r'(?<=\d)-(?=\d)'
    html_code_of_short_dash = '&#8210'
    fixed_short_dashes = regex.sub(
        short_dash_pattern,
        html_code_of_short_dash,
        string
    )
    return fixed_short_dashes


def get_nonbreaking_space_for_numbers(match_object):
    symbol_before_number = match_object.group(1)
    if regex.match(r'\s', symbol_before_number):
        str_without_end_space = match_object.group(0).rstrip()
        nonbreaking_space = '&#160'
        str_with_nonbreaking_space = str_without_end_space + nonbreaking_space
        return str_with_nonbreaking_space
    return match_object.group(0)


def add_nonbreaking_spaces(string):
    search_pattern = r'(\D)(\d+\s)(?=\p{L})'
    text_with_nonbreaking_spaces = regex.sub(
        search_pattern,
        get_nonbreaking_space_for_numbers,
        string
    )
    return text_with_nonbreaking_spaces


def delete_redundant_spaces(string):
    redundant_space_pattern = r'  +'
    text_without_redundant_spaces = regex.sub(
        redundant_space_pattern,
        ' ',
        string
    )
    return text_without_redundant_spaces


def delete_empty_lines(string):
    empty_line_pattern = r'\s\s+'
    text_without_empty_lines = regex.sub(
        empty_line_pattern,
        '\n',
        string
    )
    return text_without_empty_lines


def get_nonbreaking_space_for_short_words(match_object):
    matched_str = match_object.group(0)
    nonbreaking_space = '&#160'
    str_with_nonbreaking_space = matched_str.rstrip() + nonbreaking_space
    return str_with_nonbreaking_space


def bind_short_words_together(string):
    short_words_pattern = r'\s\p{L}{1,2} '
    text_with_bound_short_words = regex.sub(
        short_words_pattern,
        get_nonbreaking_space_for_short_words,
        # '!',
        string
    )
    return text_with_bound_short_words


def launch_typograph(content):
    content = delete_redundant_spaces(content)
    content = add_nonbreaking_spaces(content)
    content = fix_left_quotes(content)
    content = fix_right_quotes(content)
    content = substitute_hyphens_for_dashes(content)
    content = substitute_hyphens_for_short_dashes(content)
    content = delete_empty_lines(content)
    content = bind_short_words_together(content)
    return content


if __name__ == '__main__':
    text = get_text()
    text = launch_typograph(text)
    print(text)