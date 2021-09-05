import unittest
from cipher_function import affine_cipher

class TestAffineCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(affine_cipher(3, 2, 'hello world', mode='encrypt', cipher_split=False), 'XOJJS QSBJL')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(affine_cipher(3, 2, 'hello world', mode='encrypt', cipher_split=True), 'XOJJS QSBJL')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(affine_cipher(3, 2, 'hello, world!', mode='encrypt', cipher_split=False), 'XOJJS, QSBJL!')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(affine_cipher(3, 2, 'hello, world!', mode='encrypt', cipher_split=True), 'XOJJS QSBJL')

    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(affine_cipher(3, 2, 'XOJJS QSBJL', mode='decrypt'), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()