import re

# Rule 1: It removes all elements other than alphabet
def keep_only_alphabet(lines):
    return re.sub(r'[^a-zA-Z]', '', lines)

# Rule 2: It lowers the capital letter
def to_lower(line):
    return line.lower()

# Rule 3: It will replace the provided string of characters
def replace_character( lines, character_string ):
    return re.sub( character_string, '', lines)

# It will do the preprocessing operations given by the user
def preprocessing_operation(content, preprocessing_steps, character_string):
    if 1 in preprocessing_steps:
        content = keep_only_alphabet(content)
    if 2 in preprocessing_steps:
        content = to_lower(content)
    if 3 in preprocessing_steps:
        content = replace_character(content, character_string)
    return content
    



