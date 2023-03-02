def text_block( text, size = 5 ):
    """
    Arguments:
        text (str): text to block
        size (int, optional): # of characters in a block
    Returns:
        (str): text blocked into groups of specified size
    """
    
    blocked_text = '' 
    
    for character in text: 
        if len(blocked_text.replace(' ', '') ) % size == 0 and len(blocked_text) != 0:
            blocked_text += ' '

        blocked_text += character
    
    return blocked_text

def text_clean( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
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


def letter_freq(message,LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    frequencies = []
    for char in LETTERS:
        count = (message.count(char))
        frequencies.append(100 * (count/len(message)))
    return(frequencies)