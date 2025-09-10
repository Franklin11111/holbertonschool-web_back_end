#!/usr/bin/env python3
""" Basic authentication
"""

from .auth import Auth
import base64


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def __init__(self):
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        base64_authorization_header
        """
        try:
            if base64_authorization_header is None:
                return None
            elif type(base64_authorization_header) is not str:
                return None
            else:
                return base64.b64decode(base64_authorization_header).decode("utf-8")
        except:
            return None




