import unittest
from cipher_function import standart_vigenere_cipher

class TestStandartVigenereCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(standart_vigenere_cipher('cipher', 'hello world', mode='encrypt', cipher_split=False), 'JMASSNQZAK')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(standart_vigenere_cipher('cipher', 'hello world', mode='encrypt', cipher_split=True), 'JMASS NQZAK')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(standart_vigenere_cipher('cipher', 'hello, world!', mode='encrypt', cipher_split=False), 'JMASSNQZAK')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(standart_vigenere_cipher('cipher', 'hello, world!', mode='encrypt', cipher_split=True), 'JMASS NQZAK')

if __name__ == '__main__':
    unittest.main()