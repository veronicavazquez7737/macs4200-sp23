def affine(message, km, ka, encipher=True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    message = message.upper().replace(' ', '')
    
    if encipher:
        ciphertext = ''
        for char in message:
            plaintext_num = LETTERS.find(char)
            ciphertext_num = (plaintext_num * km + ka) % len(LETTERS)
            ciphertext += LETTERS[ciphertext_num]
        
        return ciphertext
    
    else:
 
        row1 = [len(LETTERS), 1, 0]
        row2 = [km, 0, 1]
    
        while row2[0] > 1:
            multiple = row1[0] // row2[0]

            row3 = [ row1[0] - multiple*row2[0], 
                     row1[1] - multiple*row2[1], 
                     row1[2] - multiple*row2[2] 
                   ]

            row1 = row2
            row2 = row3
        
        km_inverse = row2[2] % len(LETTERS)
        
        plaintext = ''
        for char in message:
            ciphertext_num = LETTERS.find(char)
            plaintext_num = ( (ciphertext_num - ka) * km_inverse) % len(LETTERS)
            plaintext += LETTERS[plaintext_num]

        return plaintext