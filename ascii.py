
def create_ascii_dict() -> dict:
    table = {}
    for i in range(0, 256):
        table[chr(i)] = str(i)
    return table