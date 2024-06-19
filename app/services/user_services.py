from typing import List
from app.models import User
from app.repositories import UserRepository

repository = UserRepository()

class UserService:
    def save(self, user: User):
        return repository.save(user)

    def update(self, user: User, id: int) -> User:
        return repository.update(user, id)

    def delete(self, user: User) -> None:
        repository.delete(user)

    def all(self) -> List[User]:
        return repository.all()

    def find(self, id: int) -> User:
        return repository.find(id)

    def find_by_username(self, username: str):
        return repository.find_by_username(username)

    def find_by_email(self, email) -> User:
        return repository.find_by_email(email)