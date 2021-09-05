import unittest
from cipher_function import shift_cipher

class TestShiftCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(shift_cipher(3, 'hello world', mode='encrypt',cipher_split=False), 'KHOOR ZRUOG')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(shift_cipher(3, 'hello world', mode='encrypt', cipher_split=True), 'KHOOR ZRUOG')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(shift_cipher(3, 'hello, world!', mode='encrypt',cipher_split=False), 'KHOOR, ZRUOG!')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(shift_cipher(3, 'hello, world!', mode='encrypt', cipher_split=True), 'KHOOR ZRUOG')

    def test_decrypt_helloworld_nosplit(self):
        self.assertEqual(shift_cipher(3, 'KHOORZRUOG', mode='decrypt'), 'HELLOWORLD')
    
    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(shift_cipher(3, 'KHOOR ZRUOG', mode='decrypt'), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()