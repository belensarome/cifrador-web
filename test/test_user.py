import unittest
from flask import current_app
from app import create_app, db
from app.models import User, UserData
from app.services import UserService

user_service = UserService()

class UserTestCase(unittest.TestCase):
    """
    Test User model
    Necesitamos aplicar principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
    YAGNI (You Aren't Gonna Need It) y SOLID (Single Responsibility Principle).
    """
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    
    def test_user(self):
        
        data = UserData()
        data.firstname = 'Pablo'
        data.lastname = 'Prats'
        data.address = 'Address 1234'
        data.city = 'San Rafael'
        data.country = 'Argentina'
        data.phone = '54260123456789'
    
        user = User(data)
        user.email = 'test@test.com'
        user.username = 'pabloprats'
        user.password = 'Qvv3r7y'

        self.assertTrue(user.email, 'test@test.com')
        self.assertTrue(user.username, 'pabloprats')
        self.assertTrue(user.password, 'Qvv3r7y')
        self.assertIsNotNone(user.data)
        self.assertTrue(user.data.address, 'Address 1234')
        self.assertTrue(user.data.firstname, 'Pablo')
        self.assertTrue(user.data.lastname, 'Prats')
        self.assertTrue(user.data.phone, '54260123456789')   
    
    def test_user_save(self):
        
        data = UserData()
        data.firstname = 'Pablo'
        data.lastname = 'Prats'
        data.address = 'Address 1234'
        data.city = 'San Rafael'
        data.country = 'Argentina'
        data.phone = '54260123456789'
    
        user = User(data)
        user.email = 'test@test.com'
        user.username = 'pabloprats'
        user.password = 'Qvv3r7y'

        user_service.save(user)
        self.assertGreaterEqual(user.id, 1)
        self.assertTrue(user.email, 'test@test.com')
        self.assertTrue(user.username, 'pabloprats')
        self.assertTrue(user.password, 'Qvv3r7y')
        self.assertIsNotNone(user.data)
        self.assertTrue(user.data.address, 'Address 1234')
        self.assertTrue(user.data.firstname, 'Pablo')
        self.assertTrue(user.data.lastname, 'Prats')
        self.assertTrue(user.data.phone, '54260123456789')
    
    def test_user_delete(self):
        
        data = UserData()
        data.firstname = 'Pablo'
        data.lastname = 'Prats'
        data.address = 'Address 1234'
        data.city = 'San Rafael'
        data.country = 'Argentina'
        data.phone = '54260123456789'
    
        user = User(data)
        user.email = 'test@test.com'
        user.username = 'pabloprats'
        user.password = 'Qvv3r7y'

        user_service.save(user)

        #borro el usuario
        user_service.delete(user)
        self.assertIsNone(user_service.find(user))
    
    def test_user_all(self):
        
        data = UserData()
        data.firstname = 'Pablo'
        data.lastname = 'Prats'
        data.address = 'Address 1234'
        data.city = 'San Rafael'
        data.country = 'Argentina'
        data.phone = '54260123456789'
    
        user = User(data)
        user.email = 'test@test.com'
        user.username = 'pabloprats'
        user.password = 'Qvv3r7y'
        user_service.save(user)

        users = user_service.all()
        self.assertGreaterEqual(len(users), 1)
    
    def test_user_find(self):
        
        data = UserData()
        data.firstname = 'Pablo'
        data.lastname = 'Prats'
        data.address = 'Address 1234'
        data.city = 'San Rafael'
        data.country = 'Argentina'
        data.phone = '54260123456789'
    
        user = User(data)
        user.email = 'test@test.com'
        user.username = 'pabloprats'
        user.password = 'Qvv3r7y'
        user_service.save(user)

        user_find = user_service.find(1)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id, user.id)
        self.assertEqual(user_find.email, user.email)



if __name__ == '__main__':
    unittest.main()