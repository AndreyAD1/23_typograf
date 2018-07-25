import re


def launch_typograph(content):
    substitute_rules = [
        ('[  ]+ # delete redundant spaces', ' '),
        (
            r'((\s|\A)\d+)(\s)(?=[а-яА-Яa-zA-Z]) # bind numbers with words',
            r'\1&#160'
        ),
        (r'[\'|"](?=\w) # fix left quotes', '&#171'),
        (r'(?<=\w)[\'|"] # fix right quotes', '&#187'),
        (r'(?<=\s)-(?=\s) # substitute hyphens for dashes', '&#8211'),
        (r'(?<=\d)-(?=\d) # replace_hyphens_in_phone_numbers', '&#8210'),
        (r'\s\s+ # delete empty lines', '\n'),
        (
            r'(?<!-)(\b\p{L}{1,2})( )(?=[а-яА-Яa-zA-Z]) # bind short words',
            r'\1&#160'
        )
    ]
    for pattern, substitute in substitute_rules:
        content = re.sub(pattern, substitute, content, flags=re.VERBOSE)
    return content


if __name__ == '__main__':
    text = 'Фалкон-9 - ракета. 234-567 телефон         тел.'
    formatted_text = launch_typograph(text)
    print(formatted_text)