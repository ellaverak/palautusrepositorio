import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UsernameAlreadyInuse(Exception):
    pass


class InvalidUsername(Exception):
    pass


class InvalidPassword(Exception):
    pass

class PasswordConfirmationfailed(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if not self._user_repository.find_by_username(username) == None:
            raise UsernameAlreadyInuse("Username already in use")

        if not re.match("[a-z]{3,}", username):
            raise InvalidUsername("Invalid username")

        if not re.match("([a-z0-9]){8,}", password):
            raise InvalidPassword("Invalid password")

        if password != password_confirmation:
            raise PasswordConfirmationfailed("Password confirmation failed")


user_service = UserService()
