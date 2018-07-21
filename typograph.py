import regex


def launch_typograph(content):
    substitute_rules = [
        # delete redundant spaces
        ('  +', ' '),
        # bind numbers with words
        (r'((\s|\A)\d+)(\s)(?=\p{L})', r'\1&#160'),
        # fix left quotes
        (r'[\'|"](?=\w)', '&#171'),
        # fix right quotes
        (r'(?<=\w)[\'|"]', '&#187'),
        # substitute hyphens for dashes
        (r'(?<=\s)-(?=\s)', '&#8211'),
        # replace_hyphens_in_phone_numbers
        (r'(?<=\d)-(?=\d)', '&#8210'),
        # delete empty lines
        (r'\s\s+', '\n'),
        # bind short words together
        (r'(?<!-)(\b\p{L}{1,2})( )(?=\p{L})', r'\1&#160')
    ]
    for pattern, substitute in substitute_rules:
        content = regex.sub(pattern, substitute, content)
    return content


if __name__ == '__main__':
    text = 'Some text.'
    edited_text = launch_typograph(text)
    print(text)