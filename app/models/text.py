from dataclasses import dataclass
from typing import List
from app import db

@dataclass(init=False, repr=True, eq=True)
class Text(db.Model):
    __tablename__ = "text"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    content: str = db.Column(db.String(1200), nullable=False)
    length: int = db.Column(db.Integer, nullable=False)
    language: str = db.Column(db.String, nullable=False)

    def save(self) -> 'Text':
        db.session.add(self)
        db.session.commit()
        return self