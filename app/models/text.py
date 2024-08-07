from dataclasses import dataclass
from typing import List
from app import db
from cryptography.fernet import Fernet

@dataclass(init=False, repr=True, eq=True)
class Text(db.Model):
    __tablename__ = "text"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    content: str = db.Column(db.String(1200), nullable=False)
    length: int = db.Column(db.Integer, nullable=False)
    language: str = db.Column(db.String, nullable=False)
    
    


