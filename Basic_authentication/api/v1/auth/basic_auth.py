#!/usr/bin/env python3
""" Basic authentication
"""

from .auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def __init__(self):
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header[6:]
