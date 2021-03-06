import unittest
from substitution_cipher import substitution_cipher

class TestAffineCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(substitution_cipher('cipher', 'hello world', mode='encrypt', cipher_split=False), 'BEJJM WMQJH')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(substitution_cipher('cipher', 'hello world', mode='encrypt', cipher_split=True), 'BEJJM WMQJH')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(substitution_cipher('cipher', 'hello, world!', mode='encrypt', cipher_split=False), 'BEJJM, WMQJH!')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(substitution_cipher('cipher', 'hello, world!', mode='encrypt', cipher_split=True), 'BEJJM WMQJH')

    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(substitution_cipher('cipher', 'BEJJM WMQJH', mode='decrypt'), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()