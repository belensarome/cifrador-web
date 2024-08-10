import unittest
from flask import current_app
from app import create_app
from app.models import User, UserData, Text
from app import db
from app.services import UserService, TextService

text_service = TextService()
user_service = UserService()

class UserTextsTestCase(unittest.TestCase):

        def setUp(self):
            self.app = create_app()
            self.app_context = self.app.app_context()
            self.app_context.push()
            self.USERNAME_PRUEBA = 'pabloprats'
            self.EMAIL_PRUEBA = 'test@test.com'
            self.PASSWORD_PRUEBA = '123456'
            self.ADDRESS_PRUEBA = 'Address 1234'
            self.FIRSTNAME_PRUEBA = 'Pablo'
            self.LASTNAME_PRUEBA = 'Prats'
            self.PHONE_PRUEBA = '54260123456789'
            self.CITY_PRUEBA = 'San Rafael'
            self.COUNTRY_PRUEBA = 'Argentina'
            self.TEXTO_PRUEBA = "Hola mundo"
            self.LANGUAGE_PRUEBA = "es"
            self.app_context.push()
            db.create_all()

        def tearDown(self):
            db.session.remove()
            db.drop_all()
            self.app_context.pop()

        def test_app(self):
            self.assertIsNotNone(current_app)

        def test_user_save(self):
            user = self.__get_user()
            user_service.save(user)
            text = self.__get_text()
            text.user_id = user.id
            text_service.save(text)
            
            self.assertEqual(user.id, text.user_id)

        def __get_user(self):
            data = UserData()
            data.firstname = self.FIRSTNAME_PRUEBA
            data.lastname = self.LASTNAME_PRUEBA
            data.phone = self.PHONE_PRUEBA
            data.address = self.ADDRESS_PRUEBA
            data.city = self.CITY_PRUEBA
            data.country = self.COUNTRY_PRUEBA

            user = User(data)
            user.username = self.USERNAME_PRUEBA
            user.email = self.EMAIL_PRUEBA
            user.password = self.PASSWORD_PRUEBA

            return user
        
        def __get_text(self):
            mytext = Text()
            mytext.content = self.TEXTO_PRUEBA
            mytext.length = len(mytext.content)
            mytext.language = self.LANGUAGE_PRUEBA
            return mytext