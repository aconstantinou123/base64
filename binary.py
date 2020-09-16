"""Module for binary conversion"""


def binary_to_base_ten(bin_num: str) -> int:
    """
    recursive function to convert a binary
    number to base ten
    param bin_num: the number to convert
    """
    dec_num = 0
    current_bin = 1
    last_index = len(bin_num) - 1
    for i in range(0, len(bin_num)):
        if bin_num[last_index - i] == '1':
            dec_num += current_bin
        current_bin = current_bin  * 2
    return dec_num


def base_ten_to_binary(base_ten_num: int) ->str:
    """
    recursive function to convert a base ten
    number to binary
    param base_ten_num: the number to convert
    """
    bin_array = ['0', '0', '0', '0', '0', '0', '0', '0']
    current_index = len(bin_array) - 1
    current_bin = 1
    def recursive_convert() -> str:
        nonlocal base_ten_num, bin_array, current_index, current_bin
        if base_ten_num > 0:
            if current_bin * 2 > base_ten_num:
                bin_array[current_index] = '1'
                base_ten_num -= current_bin
                current_bin = 1
                current_index = len(bin_array)
            else:
                current_bin = current_bin * 2
            current_index -= 1
            recursive_convert()
        return bin_array
    bin_array = recursive_convert()
    return ', '.join(bin_array).replace(', ', '')
