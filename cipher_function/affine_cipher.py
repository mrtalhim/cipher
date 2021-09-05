import helper_function as hf

def affine_cipher(key, input, mode='encrypt', cipher_split=False):
    a_key, b_key = key
    
    if mode=='encrypt':
        return encrypt(a_key, b_key, input, cipher_split=cipher_split)
    
    elif mode=='decrypt':
        return decrypt(a_key, b_key, input)

def encrypt(a_key, b_key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = [
        plain_alphabet[(a_key * plain_alphabet.index(x) + b_key) % 26]
        for x in plain_alphabet
    ]

    plaintext = hf.plaintext_prep(plaintext)
    ciphertext = ''.join([
        cipher_alphabet[plain_alphabet.index(x)]
        if x.isalpha() else x
        for x in plaintext
    ])

    return hf.present_ciphertext(ciphertext, split=cipher_split)

def decrypt(a_key, b_key, ciphertext):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = [
        plain_alphabet[(a_key * plain_alphabet.index(x) + b_key) % 26]
        for x in plain_alphabet
    ]

    ciphertext = hf.plaintext_prep(ciphertext)
    plaintext = ''.join([
        plain_alphabet[cipher_alphabet.index(x)]
        if x.isalpha() else x
        for x in ciphertext
    ])
    
    return hf.present_ciphertext(plaintext)