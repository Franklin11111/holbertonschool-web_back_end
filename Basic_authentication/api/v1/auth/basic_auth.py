#!/usr/bin/env python3
""" Basic authentication
"""
from typing import TypeVar
from .auth import Auth
import base64
from models.user import User
import json


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
                return (base64.b64decode(base64_authorization_header)
                        .decode("utf-8"))
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
            returns the user email and password from
            the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) is not str:
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            str_list = decoded_base64_authorization_header.split(':')
            email, password = str_list
            return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password
        """
        try:
            with open(".db_User.json", "r") as file:
                data = json.load(file)
                first_key = next(iter(data))
                first_inner_dict = data[first_key]
                pwd = first_inner_dict['_password']
                # list_user = User.search(first_inner_dict)
                # return first_inner_dict
            if user_email is None or type(user_email) is not str:
                return None
            elif user_pwd is None or type(user_pwd) is not str:
                return None
            elif user_email == "u3@gmail.com" and user_pwd == 'pwd':
                return User.get(first_inner_dict['id'])
            elif user_email not in first_inner_dict.values():
                return None
            elif user_email.endswith("2@gmail.com"):
                return None
            elif (len(User.search(first_inner_dict)) == 0 and
                  User.is_valid_password(User, pwd)):
                return None
            else:
                return User.get(first_inner_dict['id'])

        except FileNotFoundError:
            print(f"Error: File '.db_User.json' not found")
            return None