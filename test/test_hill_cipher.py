import unittest
import numpy as np
from hill_cipher import hill_cipher

class TestHillCipher(unittest.TestCase):

    def test_encrypt_help_nosplit(self):
        key = [['d', 'c'],
               ['d', 'f']]
        self.assertEqual(hill_cipher(key, 'help', mode='encrypt',cipher_split=False), 'HIAT')
        
    def test_encrypt_act_nosplit(self):
        key = [['g', 'n', 'u'],
               ['y', 'q', 'r'],
               ['b', 'k', 'p']]
        self.assertEqual(hill_cipher(key, 'act', mode='encrypt',cipher_split=False), 'POH')
        
    def test_encrypt_cat_nosplit(self):
        key = [['g', 'n', 'u'],
               ['y', 'q', 'r'],
               ['b', 'k', 'p']]
        self.assertEqual(hill_cipher(key, 'cat', mode='encrypt',cipher_split=False), 'FIN')

    def test_decrypt_help_nosplit(self):
        key = [['d', 'c'],
               ['d', 'f']]
        self.assertEqual(hill_cipher(key, 'HIAT', mode='decrypt'), 'HELP')

    def test_decrypt_act_nosplit(self):
        key = [['g', 'n', 'u'],
               ['y', 'q', 'r'],
               ['b', 'k', 'p']]
        self.assertEqual(hill_cipher(key, 'POH', mode='decrypt'), 'ACT')

    def test_decrypt_cat_nosplit(self):
        key = [['g', 'n', 'u'],
               ['y', 'q', 'r'],
               ['b', 'k', 'p']]
        self.assertEqual(hill_cipher(key, 'FIN', mode='decrypt'), 'CAT')

if __name__ == '__main__':
    unittest.main()