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
        if path is None:
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            return True
        new_path = path
        if not path.endswith("/"):
            new_path += "/"
        if new_path not in excluded_paths:
            return True
        elif new_path in excluded_paths:
            return False
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
