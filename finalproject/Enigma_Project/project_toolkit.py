def text_clean( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?!@#'):
    """
    Arguments:
        text (str): a piece of text for cleaning
        LETTERS (str, optional): defines the alphabet of allowable characters
    Returns:
        (str): text with only the characters also found in LETTERS
               lower-case letters in text will be made upper-case  
    """

    cleaned_text = '' 
    
    for character in text: 
        if character.upper() in LETTERS:
            cleaned_text += character.upper()
    
    return cleaned_text


def text_block(text, block = 5):
    """
    Arguments:
        text (str): a piece of text for separating into blocks of equal size, separated by a single space
        block (int, optional): defines the legth of each block
    Returns:
        (str): text identical to the text provided but divided into blocks
        
    """
    
    x = 1
    output = ''
    for char in text:
        output += char
        if x == block:
            output += ' '
            x = 0
        x += 1    
    return output        