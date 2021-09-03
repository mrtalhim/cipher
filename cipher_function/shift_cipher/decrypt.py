from cipher_function import helper_function as hf

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