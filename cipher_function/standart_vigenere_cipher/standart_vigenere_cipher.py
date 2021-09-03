from cipher_function import helper_function as hf

def encrypt(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    plaintext = hf.plaintext_prep(plaintext, alpha_only=True)
    while len(key) <= len(plaintext):
        key += key
    ciphertext = ''
    for x in range(len(plaintext)):
        cipher = hf.alphabet_index(plaintext[x], plain_alphabet) + hf.alphabet_index(key[x], plain_alphabet)
        cipher = cipher % 26
        ciphertext += plain_alphabet[cipher]
    return hf.present_ciphertext(ciphertext, split=cipher_split)