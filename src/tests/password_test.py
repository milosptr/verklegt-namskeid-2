from django.test import TestCase, tag
from django.contrib.auth.hashers import make_password, check_password


class PasswordHasherTests(TestCase):
    @tag('no_db')
    def test_password_hasher(self):
        # The password to test
        password = 'my_plain_password'

        # Hash the password
        hashed_password = make_password(password)

        # Check the password
        self.assertTrue(check_password(password, hashed_password), "The password should match the hash.")

        # Optionally, you can also check for failures
        self.assertFalse(check_password('wrong_password', hashed_password), "The password should not match the hash.")

    def test_if_password_is_correct(self):
        password = 'bcrypt_sha256$$2b$12$Slm5WlwteEey61bvqs1mKeTlAGeUIZIaIqgquLn0b787Ogk16aGaO'
        self.assertTrue(check_password('password', password), "The password should match the hash.")
