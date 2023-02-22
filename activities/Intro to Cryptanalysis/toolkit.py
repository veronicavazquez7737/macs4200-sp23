def text_clean(message, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    message = message.upper()
    output = ''
    for char in message:
        if char in LETTERS:
            output += char
    return (output)
    
def text_block(message, block = 5):
    output = ''
    num = 1
    for i in range(len(message)):
        output += message[i]
        if num % (block) == 0:
            output += ' '
            num += 1
        else:
            num += 1
        
    return(output)

def caesar(message,key):
    message = message.replace(' ','').upper()
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    for char in message:
        num = LETTERS.find(char)
        num = (num + key) % 26
        output += LETTERS[num]
    return(output)    
        
def affine(message, keyM, keyA, encipher = True):
    message = message.replace(' ','').upper()
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    for i in range(len(LETTERS)):
        if (i * keyM) % len(LETTERS) == 1:
            inverse = i
    if encipher == True:
        for char in message:
            num = LETTERS.find(char)
            num = (num * keyM + keyA) % len(LETTERS)
            output += LETTERS[num]
    else:
        for char in message:
            num = LETTERS.find(char)
            num = (inverse * (num - keyA)) % len(LETTERS)
            output += LETTERS[num]
            
    return(output)

def random(key1, key2, message):
    
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    message = message.upper()
    clean_message = ''
    for char in message:
        if char in LETTERS:
            clean_message += char
    
    key1 = key1.upper()
    clean_key1 = ''
    for char in key1:
        if char in LETTERS:
            if char not in clean_key1:
                clean_key1 += char
    
    x = LETTERS.find(key2)
    
    sub_alpha1 = clean_key1
    
    for char in LETTERS:
        if char not in sub_alpha1:
            sub_alpha1 += char
    
    y = len(LETTERS) - x
    sub_alpha = sub_alpha1[y:] + sub_alpha1[:y]
    
    output = ''
    
    for char in clean_message:
        num = LETTERS.find(char)
        output += sub_alpha[num]
    
    return(output)
    