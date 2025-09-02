#!/usr/bin/env python3
"""
Using Regex for obfuscating sensitive information
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Function for filtering sensitive information
    """
    pattern_regex = '(' + '=.*|'.join(fields) + ')'
    new_message = re.sub(pattern_regex, fields[0]+"="+redaction+separator+fields[1]+"="+redaction+separator, message)
    return new_message
