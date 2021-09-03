import unittest
from cipher_function import shift_cipher

class TestShiftCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(shift_cipher.encrypt(3, 'hello world',cipher_split=False), 'KHOOR ZRUOG')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(shift_cipher.encrypt(3, 'hello world', cipher_split=True), 'KHOOR ZRUOG')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(shift_cipher.encrypt(3, 'hello, world!',cipher_split=False), 'KHOOR, ZRUOG!')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(shift_cipher.encrypt(3, 'hello, world!', cipher_split=True), 'KHOOR ZRUOG')

    def test_decrypt_helloworld_nosplit(self):
        self.assertEqual(shift_cipher.decrypt(3, 'KHOORZRUOG'), 'HELLOWORLD')
    
    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(shift_cipher.decrypt(3, 'KHOOR ZRUOG'), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()