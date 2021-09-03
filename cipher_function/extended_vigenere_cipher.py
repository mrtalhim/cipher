import helper_function as hf

def extended_vigenere_cipher(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    plaintext = hf.plaintext_prep(plaintext)
    while len(key) <= len(plaintext):
        key += key
    ciphertext = ''
    for x in range(len(plaintext)):
        cipher = hf.alphabet_index(plaintext[x], plain_alphabet) + hf.alphabet_index(key[x], plain_alphabet)
        cipher = cipher % 26
        ciphertext += plain_alphabet[cipher]
    return hf.present_ciphertext(ciphertext, split=cipher_split)

print([chr(x) for x in range(128)])