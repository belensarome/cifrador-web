from dataclasses import dataclass, field
from typing import List
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin
from .user_data import UserData
from app import db
from app.models.relations import users_roles

@dataclass(init=False, repr=True, eq=True)
class User(SoftDeleteMixin, AuditMixin, db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column('password', db.String(255), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False) 
    #Relacion Uno a Uno bidireccional con UserData
    data = db.relationship('UserData', uselist=False, back_populates='user') # type: ignore

    #Relacion Muchos a Muchos bidireccional con Role
    #Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149 
    roles = db.relationship("Role", secondary=users_roles, back_populates='users')

    # Relación uno a muchos con text
    texts = db.relationship('Text', uselist=False, back_populates='user')

    def __init__(self, username: str = None, password: str = None, email: str = None, data: UserData = None):
        self.data = data
        self.username = username
        self.password = password
        self.email = email

    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)


    

    """
    Aplico el patrón Active Record https://www.martinfowler.com/eaaCatalog/activeRecord.html, donde el modelo se encarga de la persistencia de los datos.
    Este patrón es muy útil para aplicaciones pequeñas y medianas, pero no es recomendable para aplicaciones grandes.
    Puede llegar a contradecir los principios SOLID http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod, ya que el modelo tiene responsabilidades de persistencia y de negocio.
    
    """
