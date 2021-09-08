import helper_function as hf

def shift_cipher(key, input, mode='encrypt', cipher_split=False):
    """Python implementation of Shift Cipher

    Args:
        key (int): Key for cipher operation
        input (str): Text to encrypt/decrypt
        mode (str, optional): Selects mode to do between 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
        cipher_split (bool, optional): Selects cipher encryption output between no space if False and 5-character group if True. Defaults to False.

    Returns:
        str: text output from cipher operation
    """
    
    if mode=='encrypt':
        return encrypt(key, input, cipher_split=cipher_split)
    
    elif mode=='decrypt':
        return decrypt(key, input)

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = [
        plain_alphabet[(plain_alphabet.index(x) + key) % 26]
        for x in plain_alphabet
    ]

    plaintext = hf.plaintext_prep(plaintext)
    ciphertext = ''.join([
        cipher_alphabet[plain_alphabet.index(x)]
        if x.isalpha() else x
        for x in plaintext
    ])
    
    return hf.present_ciphertext(ciphertext, split=cipher_split)

def decrypt(key, ciphertext):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = [
        plain_alphabet[(plain_alphabet.index(x) - key) % 26]
        for x in plain_alphabet
    ]

    ciphertext = hf.plaintext_prep(ciphertext)
    plaintext = ''.join([
        cipher_alphabet[plain_alphabet.index(x)]
        if x.isalpha() else x
        for x in ciphertext
    ])

    return hf.present_ciphertext(plaintext)

if __name__ == "__main__":
    shift_cipher()