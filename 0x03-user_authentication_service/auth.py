#!/usr/bin/env python3
""" Auth Module for hashing
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt and returns
    the hashed password as bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
