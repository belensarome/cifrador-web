import unittest
from flask import current_app
from app import create_app, db
from app.models import Text

class TextTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_text(self):
        mytext = Text()
        mytext.content = "Hola mundo"
        mytext.length = len(mytext.content)
        mytext.language = "es"
        mytext.save()

        self.assertIsNotNone(mytext)
        self.assertEqual(mytext.content, "Hola mundo")

    

if __name__ == '__main__':
    unittest.main()