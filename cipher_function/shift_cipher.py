import helper_function as hf

def shift_cipher(key, plaintext, cipher_split=False):
    plain_alphabet = hf.alphabet_init()
    cipher_alphabet = [plain_alphabet[(plain_alphabet.index(x) + key) % 26] for x in plain_alphabet]
    plaintext = hf.plaintext_prep(plaintext)
    ciphertext = ''.join([cipher_alphabet[plain_alphabet.index(x)] if x.isalpha() else x for x in plaintext])
    return hf.present_ciphertext(ciphertext, split=cipher_split)