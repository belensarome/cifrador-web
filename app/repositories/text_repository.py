from app.models import Text
from app import db

class TextRepository:
    def save(self, text:Text) -> 'Text':
        db.session.add(text)
        db.session.commit()
        return text

    def delete(self, text:Text) -> None:
        db.session.delete(text)
        db.session.commit()