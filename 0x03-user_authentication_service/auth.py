#!/usr/bin/env python3
""" Auth Module for hashing
"""

from db import DB
from user import User
from typing import Optional
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """
        Hashes a password with bcrypt and returns
        the hashed password as bytes.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with the given email and password.
        If a user with the given email already exists,
        raises a ValueError.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return user
        except InvalidRequestError:
            raise

    def valid_login(self, email: str, password: str) -> bool:
        """Check if login credentials are valid."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8'))
        except NoResultFound:
            return False
