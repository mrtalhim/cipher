import numpy as np
import helper_function as hf

def playfair_cipher(key, input, mode='encrypt', cipher_split=False):
    """Python implementation of Playfair Cipher

    Args:
        key (str): Key for cipher operation. Must be in alphabet (a-z). If key doesn't have include all alphabet, it will be added
        mode (str, optional): Selects mode to do between 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
        cipher_split (bool, optional): Selects cipher encryption output between no space if False and 5-character group if True. Defaults to False.

    Returns:
        str: text output from cipher operation
    """
    
    input = list(hf.plaintext_prep(input, alpha_only=True))
    
    # split any character duplicates
    for x in range(len(input) - 1):
        a = input[x]
        b = input[x + 1]
        if a == b:
            input.insert(x + 1, 'x')

    # slice input into pair of characters
    input_sliced = []
    
    for x in range(0, len(input), 2):
        slice = input[x:x+2]
        if len(slice) == 1:
            slice.append('x')
        input_sliced.append(slice)
    
    if mode=='encrypt':
        return encrypt(key, input_sliced, cipher_split=cipher_split)
    
    elif mode=='decrypt':
        return decrypt(key, input_sliced)

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = dict.fromkeys(x for x in key)
    cipher_alphabet = list(cipher_alphabet)
    ciphertext = ''

    for x in plain_alphabet:
        if x not in cipher_alphabet and x != 'j':
            cipher_alphabet.append(x)
            
    cipher_matrix = [cipher_alphabet[i:i+5]
                     for i in range(0, 25, 5)]
    
    for i in plaintext:
        x_1, x_2 = hf.matrix_alphabet_index(i[0], cipher_matrix)
        y_1, y_2 = hf.matrix_alphabet_index(i[1], cipher_matrix)
        
        # pair in same row shift to the right
        if x_1 == y_1:
            x_2 = (x_2 + 1) % 5
            y_2 = (y_2 + 1) % 5
        
        # pair in same column shift below
        elif x_2 == y_2:
            x_1 = (x_1 + 1) % 5
            y_1 = (y_1 + 1) % 5
        
        # pair in a square
        else:
            x_1, y_1 = y_1, x_1
            
        ciphertext += cipher_matrix[x_1][x_2] + cipher_matrix[y_1][y_2]
    
    return hf.present_ciphertext(ciphertext, split=cipher_split)

def decrypt(key, ciphertext):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = dict.fromkeys(x for x in key)
    cipher_alphabet = list(cipher_alphabet)
    plaintext = ''

    for x in plain_alphabet:
        if x not in cipher_alphabet and x != 'j':
            cipher_alphabet.append(x)
            
    cipher_matrix = [cipher_alphabet[i:i+5]
                     for i in range(0, 25, 5)]
    
    for i in ciphertext:
        x_1, x_2 = hf.matrix_alphabet_index(i[0], cipher_matrix)
        y_1, y_2 = hf.matrix_alphabet_index(i[1], cipher_matrix)
        
        # pair in same row shift to the right
        if x_1 == y_1:
            x_2 = (x_2 - 1) % 5
            y_2 = (y_2 - 1) % 5
        
        # pair in same column shift below
        elif x_2 == y_2:
            x_1 = (x_1 - 1) % 5
            y_1 = (y_1 - 1) % 5
        
        # pair in a square
        else:
            x_1, y_1 = y_1, x_1
            
        plaintext += cipher_matrix[x_1][x_2] + cipher_matrix[y_1][y_2]
    
    return hf.present_ciphertext(plaintext)
    
# if __name__ == "__main__":
#     playfair_cipher()
    
ciphertext = playfair_cipher('cipher', 'hello world', mode='encrypt')
print(ciphertext)
plaintext = playfair_cipher('cipher', ciphertext, mode='decrypt')
print(plaintext)