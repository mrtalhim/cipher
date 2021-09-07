import helper_function as hf

def substitution_cipher(key, input, mode='encrypt', cipher_split=False):
    """Python implementation of Substitution Cipher

    Args:
        key (str): Key for cipher operation. Must be in alphabet (a-z). If key doesn't have include all alphabet, it will be added
        input (str): Text to encrypt/decrypt
        mode (str, optional): Selects mode to do between 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
        cipher_split (bool, optional): Selects cipher encryption output between no space if False and 5-character group if True. Defaults to False.

    Returns:
        str: text output from cipher operation
    """
    
    key = hf.plaintext_prep(key, alpha_only=True)
    
    if mode=='encrypt':
        return encrypt(key, input, cipher_split=cipher_split)
    
    elif mode=='decrypt':
        return decrypt(key, input)

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    plaintext = hf.plaintext_prep(plaintext)
    cipher_alphabet = dict.fromkeys(x for x in key)
    cipher_alphabet = list(cipher_alphabet)

    for x in plain_alphabet:
        if x not in cipher_alphabet:
            cipher_alphabet.append(x)

    ciphertext = ''.join([
        cipher_alphabet[plain_alphabet.index(x)]
        if x.isalpha() else x
        for x in plaintext
    ])
    
    return hf.present_ciphertext(ciphertext, split=cipher_split)

def decrypt(key, ciphertext):
    plain_alphabet = hf.alphabet_init()
    ciphertext = hf.plaintext_prep(ciphertext)
    cipher_alphabet = dict.fromkeys(x for x in key)
    cipher_alphabet = list(cipher_alphabet)

    for x in plain_alphabet:
        if x not in cipher_alphabet:
            cipher_alphabet.append(x)

    plaintext = ''.join([
        plain_alphabet[cipher_alphabet.index(x)]
        if x.isalpha() else x
        for x in ciphertext
    ])
    
    return hf.present_ciphertext(plaintext)

if __name__ == "__main__":
    substitution_cipher()