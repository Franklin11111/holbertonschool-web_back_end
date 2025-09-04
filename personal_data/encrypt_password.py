#!/usr/bin/env python3
"""
Using bcrypt for encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Function to salt and hash password and to
    return it as byte string """
    b_password = password.encode(encoding="utf-8")
    hashed = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function to check if hashed password
        matches original password in bytes """
    b_password = password.encode(encoding="utf-8")
    if bcrypt.checkpw(b_password, hashed_password):
        return True
    else:
        return False
