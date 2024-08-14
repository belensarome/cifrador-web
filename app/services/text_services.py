from app.models import Text
from app.repositories import TextRepository

repository = TextRepository()

class TextService:
    def save(self, text:Text):
        return repository.save(text)
    
    def delete(self, text:Text):
        repository.delete(text)
    
    def find(self, id: int):
        return repository.find(id)

    def all(self):
        return repository.all()

    def find_by(self, **kwargs):
        return repository.find_by(kwargs)
        return db.session.query(Text).filter_by(**kwargs).all()