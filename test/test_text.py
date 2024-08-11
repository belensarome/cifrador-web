import unittest
from flask import current_app
from app import create_app, db
from app.models import Text
from app.services import TextService
from app.services import EncryptService
from cryptography.fernet import Fernet

text_service = TextService()
encrypt_service = EncryptService()

class TextTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.TEXTO_PRUEBA = "Hola mundo"
        self.LANGUAGE_PRUEBA = "es"
        self.KEY = "1234hola"

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_text(self):
        mytext = Text()
        mytext.content = self.TEXTO_PRUEBA
        mytext.length = len(mytext.content)
        mytext.language = self.LANGUAGE_PRUEBA
        text_service.save(mytext)

        self.assertIsNotNone(mytext)
        self.assertEqual(mytext.content, self.TEXTO_PRUEBA)
        self.assertEqual(mytext.language, self.LANGUAGE_PRUEBA)
    
    def test_encrypt(self):
        
        mytext = self.__get_text()
        
        key = encrypt_service.generate_fernet_key()
        encrypt_service.encrypt(mytext, key)
        self.assertNotEqual(mytext.content, self.TEXTO_PRUEBA)
    
    def test_encrypt_defined_key(self):
        
        mytext = self.__get_text()
        
        key = encrypt_service.generate_fernet_key(self.KEY)
        encrypt_service.encrypt(mytext, key)
        self.assertNotEqual(mytext.content, self.TEXTO_PRUEBA)

    def test_decrypt(self):
        mytext = self.__get_text()
        
        key = encrypt_service.generate_fernet_key()
        encrypt_service.encrypt(mytext, key)
        encrypt_service.decrypt(mytext, key)
        self.assertEqual(mytext.content, self.TEXTO_PRUEBA)

    def test_decrypt_defined_key(self):
        mytext = self.__get_text()
        
        key = encrypt_service.generate_fernet_key(self.KEY)
        encrypt_service.encrypt(mytext, key)
        encrypt_service.decrypt(mytext, key)
        self.assertEqual(mytext.content, self.TEXTO_PRUEBA)

    def __get_text(self):
        mytext = Text()
        mytext.content = self.TEXTO_PRUEBA
        mytext.length = len(mytext.content)
        mytext.language = self.LANGUAGE_PRUEBA
        return mytext


if __name__ == '__main__':
    unittest.main()