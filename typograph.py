import regex


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
    dash_pattern = r'(?<=\s)-(?=\s)'
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


def bind_numbers_with_words(string):
    search_pattern = r'((\s|\A)\d+)(\s)(?=\p{L})'
    text_with_nonbreaking_spaces = regex.sub(
        search_pattern,
        r'\1&#160',
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


def bind_short_words_together(string):
    short_words_pattern = r'(?<!-)(\b\p{L}{1,2})( )(?=\p{L})'
    text_with_bound_short_words = regex.sub(
        short_words_pattern,
        r'\1&#160',
        string
    )
    return text_with_bound_short_words


def launch_typograph(content):
    content = delete_redundant_spaces(content)
    content = bind_numbers_with_words(content)
    content = fix_left_quotes(content)
    content = fix_right_quotes(content)
    content = substitute_hyphens_for_dashes(content)
    content = substitute_hyphens_for_short_dashes(content)
    content = delete_empty_lines(content)
    content = bind_short_words_together(content)
    return content


if __name__ == '__main__':
    text = '2016 ujl. Погоди-ка. Он - сумасшедший! 1984 год. Фалкон-9 взлетел 289 ! Я не ем много.'
    text = launch_typograph(text)
    print(text)