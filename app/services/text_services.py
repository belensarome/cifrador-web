from app.models import Text
from app.repositories import TextRepository

repository = TextRepository()

class TextService:
    def save(self, text:Text):
        return repository.save(text)
    
    def delete(self, text:Text):
        repository.delete(text)