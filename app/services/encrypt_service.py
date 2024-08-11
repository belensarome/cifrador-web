from app.models import Text
from app.services import TextService
from cryptography.fernet import Fernet
import base64

text_service = TextService()

class EncryptService:
    KEY_SIZE = 32
    def generate_fernet_key(self, key:str = None):
        if key is None:
            return Fernet.generate_key()
        return base64.urlsafe_b64encode(key.encode().ljust(self.KEY_SIZE, b"\0"))
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