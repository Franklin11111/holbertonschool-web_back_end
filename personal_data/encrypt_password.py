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
