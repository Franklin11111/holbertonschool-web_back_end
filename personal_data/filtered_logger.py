#!/usr/bin/env python3
"""
Using Regex for obfuscating sensitive information
"""
import sys
from typing import List
import re
import logging
from datetime import date


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """    Function for formating filtered information    """
        message = self.filter_datum(self.fields, redaction=self.REDACTION,
                                    message=record.msg,
                                    separator=self.SEPARATOR)
        return (f"[HOLBERTON] {record.name} {record.levelname} "
                f"{date.today()}-15s:"
                f" {message}")

    def filter_datum(self, fields: List[str], redaction: str, message: str,
                     separator: str) -> str:
        """    Function for filtering sensitive information    """
        new_fields = []
        for m in message.split(separator):
            new_fields.append(re.sub('(' + '=.*|'.join(fields) + '=.*)',
                                     f"{m[0:m.find('=')]}={redaction}", m)) \
                if m[0:m.find('=')] in fields else new_fields.append(m)
        return separator.join(new_fields)

PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'ip')

def get_logger() -> logging.Logger:
    logger = logging.getLogger('user_data')
    logger.setLevel('INFO')
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger