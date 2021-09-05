import string
import numpy as np

def alphabet_init():
    alphabet = list(string.ascii_lowercase)
    return alphabet

def alphabet_index(char, alphabet):
    return alphabet.index(char)

def plaintext_prep(plaintext, alpha_only=False):
    plaintext = plaintext.lower()
    if alpha_only:
        plaintext = ''.join([x for x in plaintext if x.isalpha()])
    return plaintext

def present_ciphertext(ciphertext, split=False):
    ciphertext = ciphertext.upper()
    if split:
        n = 5
        ciphertext = ''.join([x for x in ciphertext if x.isalpha()])
        ciphertext = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]
        ciphertext = ' '.join(list(ciphertext))
    return ciphertext
