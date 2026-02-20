import unittest
from PP1 import verify_password

class TestVerifyPassword(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(verify_password("ValidPassword123!@#"))

    def test_invalid_password_with_spaces(self):
        self.assertFalse(verify_password("invalid password"))

    def test_short_password(self):
        self.assertFalse(verify_password("short"))

    def test_no_uppercase(self):
        self.assertFalse(verify_password("noupper123!@#"))

    def test_no_lowercase(self):
        self.assertFalse(verify_password("NOLOWER123!@#"))

    def test_no_digit(self):
        self.assertFalse(verify_password("NoDigit!@#LOWERUPPER"))

    def test_no_special(self):
        self.assertFalse(verify_password("NoSpecial123LOWERUPPER"))

if __name__ == '__main__':
    unittest.main()
