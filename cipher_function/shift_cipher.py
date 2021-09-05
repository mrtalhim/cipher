import helper_function as hf

def shift_cipher(key, input, mode='encrypt', cipher_split=False):
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