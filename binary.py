
def base_ten_to_binary(base_ten_num: int) -> str:
    empty_bin_dict = {}
    current_bin = 1
    def recursive_bin(base_ten_num: int, current_bin: int, bin_dict: dict):
        if base_ten_num > 0:
            if current_bin * 2 > base_ten_num:
                bin_dict[str(current_bin)] = 1
                base_ten_num -= current_bin
                current_bin = 1
                recursive_bin(base_ten_num,current_bin, bin_dict)
            else:
                bin_dict[str(current_bin)] = 0
                current_bin = current_bin * 2
                recursive_bin(base_ten_num,current_bin, bin_dict)
        return bin_dict
    bin_dict = recursive_bin(base_ten_num, current_bin, empty_bin_dict)
    bin_arr = []
    for _, v in bin_dict.items():
        bin_arr.insert(0, str(v))
    while len(bin_arr) < 8:
        bin_arr.insert(0, '0')
    bin_string = ''
    for i in bin_arr:
        bin_string += i
    return bin_string

def binary_to_base_ten(bin_num: str) -> int:
    dec_num = 0
    current_bin = 1
    last_index = len(bin_num) - 1
    for i in range(0, len(bin_num)):
        if bin_num[last_index - i] == '1':
            dec_num += current_bin
        current_bin = current_bin  * 2
    return dec_num
