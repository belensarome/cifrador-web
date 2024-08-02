from dataclasses import dataclass, field
from typing import List
from .user_data import UserData
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass(init=False, repr=True, eq=True)
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    __password: str = db.Column('password', db.String(255), nullable=False)
    password: str = field(init=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False) 
    data = db.relationship('UserData', uselist=False, back_populates='user') # type: ignore

    def __init__(self, user_data: UserData = None):
        self.data = user_data

    def __post_init__(self):
        self.password = self.__password
    
    @property
    def password(self):
        raise AttributeError('password: campo de lectura no permitida')
    
    @password.setter
    def password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.__password, password)
    """
    Aplico el patrón Active Record https://www.martinfowler.com/eaaCatalog/activeRecord.html, donde el modelo se encarga de la persistencia de los datos.
    Este patrón es muy útil para aplicaciones pequeñas y medianas, pero no es recomendable para aplicaciones grandes.
    Puede llegar a contradecir los principios SOLID http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod, ya que el modelo tiene responsabilidades de persistencia y de negocio.
    
    """
