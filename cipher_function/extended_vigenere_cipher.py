import helper_function as hf

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