import unittest
from shift_cipher import shift_cipher

class TestShiftCipher(unittest.TestCase):

    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(shift_cipher(3, 'hello world', mode='encrypt',cipher_split=False), 'KHOOR ZRUOG')

    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(shift_cipher(3, 'hello world', mode='encrypt', cipher_split=True), 'KHOOR ZRUOG')

    def test_encrypt_helloworld_nosplit_specialcharacter(self):
        self.assertEqual(shift_cipher(3, 'hello, world!', mode='encrypt',cipher_split=False), 'KHOOR, ZRUOG!')

    def test_encrypt_helloworld_withsplit_specialcharacter(self):
        self.assertEqual(shift_cipher(3, 'hello, world!', mode='encrypt', cipher_split=True), 'KHOOR ZRUOG')
        
    def test_encrypt_quickfox_nosplit(self):
        self.assertEqual(shift_cipher(3, 'The quick brown fox jumps over the lazy dog', mode='encrypt',cipher_split=False), 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ')
        
    def test_encrypt_quickfox_withsplit(self):
        self.assertEqual(shift_cipher(3, 'The quick brown fox jumps over the lazy dog', mode='encrypt',cipher_split=True), 'WKHTX LFNEU RZQIR AMXPS VRYHU WKHOD CBGRJ')

    def test_decrypt_helloworld_nosplit(self):
        self.assertEqual(shift_cipher(3, 'KHOORZRUOG', mode='decrypt'), 'HELLOWORLD')
    
    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(shift_cipher(3, 'KHOOR ZRUOG', mode='decrypt'), 'HELLO WORLD')
        
    def test_decrypt_quickfox_nosplit(self):
        self.assertEqual(shift_cipher(3, 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ', mode='decrypt'), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
        
    def test_decrypt_quickfox_withsplit(self):
        self.assertEqual(shift_cipher(3, 'WKHTX LFNEU RZQIR AMXPS VRYHU WKHOD CBGRJ', mode='decrypt'), 'THEQU ICKBR OWNFO XJUMP SOVER THELA ZYDOG')

if __name__ == '__main__':
    unittest.main()