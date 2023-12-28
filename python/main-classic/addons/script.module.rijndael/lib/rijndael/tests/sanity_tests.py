import unittest

from rijndael.cipher.crypt import new
from rijndael.cipher.blockcipher import MODE_CBC


class RijndaelEqualityTestCase(unittest.TestCase):
    """
        Tests whether encryption/decryption have
            relating results.
    """

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)


    def setUp(self):
        self.key = 'thisisatestkeywhichis32byteslong'
        self.iv = 'thisisatestvecwhichis32byteslong'
        self.blocksize = 32


    def test_sanity_cbc_mode(self):
        string = 'thisisateststringwhichis32bytesl'
        rijndael_e = new(self.key, MODE_CBC, self.iv, blocksize=self.blocksize)
        encrypted = rijndael_e.encrypt(string)
        rijndael_d = new(self.key, MODE_CBC, self.iv, blocksize=self.blocksize)
        decypted = rijndael_d.decrypt(encrypted)
        self.assertEquals(string, decypted)
