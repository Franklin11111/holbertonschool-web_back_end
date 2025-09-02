#!/usr/bin/env python3
"""
Using Regex for obfuscating sensitive information
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """    Function for filtering sensitive information    """
    new_fields = []
    for m in message.split(';'):
        new_fields.append(re.sub('(' + '=.*|'.join(fields) + '=.*)', f"{m[0:m.find('=')]}={redaction}", m)) \
            if m[0:m.find('=')] in fields else new_fields.append(m)
    return ';'.join(new_fields)
