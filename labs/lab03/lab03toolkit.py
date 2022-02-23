def text_clean( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Arguments:
        text (str): a piece of text for cleaning
    Returns:
        (str): text with only the characters also found in LETTERS
               lower-case letters in text will be made upper-case  
    """
    
    cleaned_text = ''
    
    for character in text:
        if character.upper() in LETTERS:
            cleaned_text += character.upper()
    
    return cleaned_text