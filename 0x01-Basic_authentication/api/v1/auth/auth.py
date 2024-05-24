#!/usr/bin/env python3
""" Authorization Model """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authorization class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if path requires authentication """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Identifies current authorized user """
        return None
