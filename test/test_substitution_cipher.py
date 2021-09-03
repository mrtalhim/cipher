import unittest
from cipher_function import substitution_cipher

class TestAffineCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(substitution_cipher.encrypt('cipher', 'hello world', cipher_split=False), 'BEJJM WMQJH')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(substitution_cipher.encrypt('cipher', 'hello world', cipher_split=True), 'BEJJM WMQJH')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(substitution_cipher.encrypt('cipher', 'hello, world!', cipher_split=False), 'BEJJM, WMQJH!')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(substitution_cipher.encrypt('cipher', 'hello, world!', cipher_split=True), 'BEJJM WMQJH')

    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(substitution_cipher.decrypt('cipher', 'BEJJM WMQJH'), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()