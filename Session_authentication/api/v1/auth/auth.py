#!/usr/bin/env python3
"""
    Auth module
"""
from typing import List, TypeVar
from flask import request, jsonify
import os


class Auth:
    """Auth class
    """
    def __init__(self):
        self.request = request
    # def get(self):
    #     authorization = request.headers.get("Authorization")
    #     return jsonify({
    #         'Authorization': authorization
    #     })

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
        Check authorization header
        """
        author = None
        if self.request.headers.get("Authorization"):
            author = self.request.headers.get("Authorization")
        if request is None:
            return None
        elif not author:
            return None
        else:
            return author

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Check current user
        """
        return None

    def session_cookie(self, request=None):
        """ Returns the value of the session cookie from the request
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')

        return request.cookies.get(session_name)
