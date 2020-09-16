"""Module for conversion of strings to base64"""
from binary import base_ten_to_binary, binary_to_base_ten
from ascii import create_ascii_dict

CHAR_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '+', '/']


def create_base64_dict() -> dict:
    """
    creates base64 lookup dict from
    list of characters
    """
    table = {}
    for i in range(0, 64):
        table[str(i)] = CHAR_LIST[i]
    return table


def string_to_base64(string: str):
    """
    convert string to base64.
    """
    ascii_dict = create_ascii_dict()
    bin_list = []
    for i in string:
        ascii_num = ascii_dict[i]
        bin = base_ten_to_binary(int(ascii_num))
        bin_list.append(bin)
    bin_string = ', '.join(bin_list).replace(', ', '')
    sextet_list = split_str_into_groups_of_three(bin_string)
    base_ten_list = [str(binary_to_base_ten(i))
                     for i in sextet_list]
    base_64_dict = create_base64_dict()
    base64_list = [base_64_dict[i]
                   for i in base_ten_list]
    return ', '.join(base64_list).replace(', ', '')

def split_str_into_groups_of_three(string: str) -> list:
    """
    splits a string into list containing
    groups of six binary characters
    """
    result_list = []
    sextet = ''
    for i in range(0, len(string)):
        sextet += str(string[i])
        if len(sextet) >= 6:
            result_list.append(sextet)
            sextet = ''
    return result_list
