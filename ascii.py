"""Module for creation of ascii lookup dict"""


def create_ascii_dict() -> dict:
    """
    creates ascii dict
    """
    table = {}
    for i in range(0, 256):
        table[chr(i)] = str(i)
    return table
