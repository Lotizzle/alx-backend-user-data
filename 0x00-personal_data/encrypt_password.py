#!/usr/bin/env python3
""" Encrypting passwords module """

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and return the hashed password.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
