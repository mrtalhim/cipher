import unittest
from playfair_cipher import playfair_cipher

class TestPlayfairCipher(unittest.TestCase):
    
    def test_encrypt_helloworld_nosplit(self):
        self.assertEqual(playfair_cipher('cipher', 'hello world', mode='encrypt', cipher_split=False), 'ECSPSGQVGBYB')
        
    def test_encrypt_helloworld_withsplit(self):
        self.assertEqual(playfair_cipher('cipher', 'hello world', mode='encrypt', cipher_split=True), 'ECSPS GQVGB YB')
        
    def test_encrypt_playfairexample_nosplit(self):
        self.assertEqual(playfair_cipher('playfair example', 'Hide the gold in the tree stump', mode='encrypt', cipher_split=False), 'MBODBZDXANEBUKMDIUXMOMUVFI')
        
    def test_encrypt_playfairexample_withsplit(self):
        self.assertEqual(playfair_cipher('playfair example', 'Hide the gold in the tree stump', mode='encrypt', cipher_split=True), 'MBODB ZDXAN EBUKM DIUXM OMUVF I')
        
    def test_decrypt_helloworld_nosplit(self):
        self.assertEqual(playfair_cipher('cipher', 'ECSPSGQVGBYB', mode='decrypt', cipher_split=False), 'HELXLOWORLDX')
        
    def test_decrypt_helloworld_withsplit(self):
        self.assertEqual(playfair_cipher('cipher', 'ECSPS GQVGB YB', mode='decrypt', cipher_split=False), 'HELXLOWORLDX')
        
    def test_decrypt_playfairexample_nosplit(self):
        self.assertEqual(playfair_cipher('playfair example', 'MBODBZDXANEBUKMDIUXMOMUVFI', mode='decrypt', cipher_split=False), 'HIDETHEGOLDINTHETREXESTUMP')
        
    def test_decrypt_playfairexample_withsplit(self):
        self.assertEqual(playfair_cipher('playfair example', 'MBODB ZDXAN EBUKM DIUXM OMUVF I', mode='decrypt', cipher_split=False), 'HIDETHEGOLDINTHETREXESTUMP')
    
if __name__ == '__main__':
    unittest.main()