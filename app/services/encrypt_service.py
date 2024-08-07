from app.models import Text
from app.services import TextService
from cryptography.fernet import Fernet

text_service = TextService()

class EncryptService:
    def encrypt(self, text: Text, key):
        f = Fernet(key)
        encrypted_content = f.encrypt(text.content.encode())
        text.content = encrypted_content.decode()
        text_service.save(text)

    def decrypt(self, text:Text, key):
        f = Fernet(key)
        decrypted_content = f.decrypt(text.content)
        text.content = decrypted_content.decode()
        text_service.save(text)