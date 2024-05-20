#!/usr/bin/env python3
"""
This module contains a function called filter_datum
that returns the log message obfuscated.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated based on the provided fields."""
    for field in fields:
        message = re.sub(fr'{field}=[^{separator}]*',
                         f'{field}={redaction}', message)
    return message
