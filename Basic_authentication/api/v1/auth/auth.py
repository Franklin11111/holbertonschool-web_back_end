#!/usr/bin/env python3
"""
    Auth module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Check authentication header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Check current user
        """
        return None
