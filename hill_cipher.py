import numpy as np
import helper_function as hf

def hill_cipher(key, input, mode='encrypt', cipher_split=False):
    """Python implementation of Hill Cipher

    Args:
        key (list(list(str))): Key for cipher operation. Must be size nxn and inversible
        input (str): Text to encrypt/decrypt
        mode (str, optional): Selects mode to do between 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
        cipher_split (bool, optional): Selects cipher encryption output between no space if False and 5-character group if True. Defaults to False.

    Returns:
        str: text output from cipher operation
    """
    
    size = len(key)
    alphabet = hf.alphabet_init()
    key_np = []
    
    for x in range(size):
        row = []
        for y in range(size):
            char = hf.alphabet_index(key[x][y].lower(), alphabet)
            row.append(char)
        key_np.append(row)
        
    key_np = np.array(key_np).T
    
    if mode=='encrypt':
        return encrypt(key_np, input, cipher_split=cipher_split)
    
    elif mode=='decrypt':
        return decrypt(key_np, input)
        # return decrypt(key_np, input)

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    plaintext = hf.plaintext_prep(plaintext, alpha_only=True)
    plaintext = [hf.alphabet_index(x, plain_alphabet)
                 for x in plaintext
                 if x.isalpha()]
    size = key.shape[0]
    plaintext_split = []
    ciphertext = []
    
    for i in range(0, len(plaintext), size):
        vector = plaintext[i:i+size]
        if len(vector) < size:
            vector.append(hf.alphabet_index('z', plain_alphabet))
        plaintext_split.append(vector)
    
    for i in range(len(plaintext_split)):
        vector = np.array(plaintext_split[i])
        cipher = np.dot(key, vector) % len(plain_alphabet)
        cipher = cipher.tolist()
        for j in cipher:
            ciphertext.append(plain_alphabet[j])
    
    ciphertext = ''.join(ciphertext)
    return hf.present_ciphertext(ciphertext, split=cipher_split)

def decrypt(key, ciphertext):
    plain_alphabet = hf.alphabet_init()
    ciphertext = hf.plaintext_prep(ciphertext, alpha_only=True)
    ciphertext = [hf.alphabet_index(x, plain_alphabet)
                 for x in ciphertext
                 if x.isalpha()]
    size = key.shape[0]
    ciphertext_split = []
    plaintext = []
    key = np.linalg.inv(key) * \
          np.linalg.det(key) * \
          hf.mod_inverse(np.linalg.det(key), len(plain_alphabet)) % \
          len(plain_alphabet)
    key = np.around(key).astype(int)
    
    for i in range(0, len(ciphertext), size):
        vector = ciphertext[i:i+size]
        if len(vector) < size:
            vector.append(hf.alphabet_index('z', plain_alphabet))
        ciphertext_split.append(vector)
    
    for i in range(len(ciphertext_split)):
        vector = np.array(ciphertext_split[i])
        plain = np.dot(key, vector) % len(plain_alphabet)
        plain = plain.tolist()
        for j in plain:
            plaintext.append(plain_alphabet[j])
    
    plaintext = ''.join(plaintext)
    return hf.present_ciphertext(plaintext)
    
if __name__ == "__main__":
    hill_cipher()