import helper_function as hf

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    plaintext = hf.plaintext_prep(plaintext)
    cipher_alphabet = {x for x in key}
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
    cipher_alphabet = {x for x in key}
    cipher_alphabet = list(cipher_alphabet)
    
    for x in plain_alphabet:
        if x not in cipher_alphabet:
            cipher_alphabet.append(x)

    plaintext = ''.join([
        plain_alphabet[ciphertext.index(x)]
        if x.isalpha() else x
        for x in ciphertext
    ])
    
    return hf.present_ciphertext(plaintext)