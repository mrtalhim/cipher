import string
import numpy as np
import PySimpleGUI as sg

def alphabet_init():
    alphabet = list(string.ascii_lowercase)
    return alphabet

def alphabet_index(char, alphabet):
    return alphabet.index(char)

def matrix_alphabet_index(char, matrix_alphabet):
    for x in matrix_alphabet:
        for y in x:
            if char in y:
                return matrix_alphabet.index(x), x.index(y)

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

def collapse(layout, key, visible):
    return sg.pin(sg.Column(layout, key=key, visible=visible))
        
def mod_inverse(a, m) : 
    a, m = int(a), int(m)
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
    