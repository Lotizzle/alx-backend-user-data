#!/usr/bin/env python3
""" Authorization Model """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authorization class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if path requires authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Identifies current authorized user """
        return None
