import unittest
from flask import current_app
from app import create_app, db
from app.models import Text
from cryptography.fernet import Fernet

class TextTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_text(self):
        mytext = Text()
        mytext.content = "Hola mundo"
        mytext.length = len(mytext.content)
        mytext.language = "es"
        mytext.save()

        self.assertIsNotNone(mytext)
        self.assertEqual(mytext.content, "Hola mundo")
    
    def test_encrypt(self):
        
        mytext = self.__get_text()
        
        key = Fernet.generate_key()
        mytext.encrypt(key)
        self.assertNotEqual(mytext.content, b"Hola mundo")

    def test_decrypt(self):
        mytext = self.__get_text()
        
        key = Fernet.generate_key()
        mytext.encrypt(key)
        mytext.decrypt(key)
        self.assertEqual(mytext.content, b"Hola mundo")

    def __get_text(self):
        mytext = Text()
        mytext.content = b"Hola mundo"
        mytext.length = len(mytext.content)
        mytext.language = "es"
        return mytext


if __name__ == '__main__':
    unittest.main()