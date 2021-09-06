import helper_function as hf

def extended_vigenere_cipher(key, input, mode='encrypt', cipher_split=False):
    """Python implementation of Vigenere Cipher for binary file input with ASCII key

    Args:
        key (str): Key for cipher operation.
        input (str): Text to encrypt/decrypt
        mode (str, optional): Selects mode to do between 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
        cipher_split (bool, optional): Selects cipher encryption output between no space if False and 5-character group if True. Defaults to False.

    Returns:
        str: text output from cipher operation
    """
    if mode=='encrypt':
        return encrypt(key, input, cipher_split=cipher_split)
    
    elif mode=='decypt':
        return None

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = [chr(x) for x in range(128)]

    while len(key) <= len(plaintext):
        key += key
    ciphertext = ''

    for x in range(len(plaintext)):
        cipher = hf.alphabet_index(plaintext[x], plain_alphabet) + hf.alphabet_index(key[x], plain_alphabet)
        cipher = cipher % 26
        ciphertext += plain_alphabet[cipher]
    
    return ciphertext

if __name__ == "__main__":
    extended_vigenere_cipher()