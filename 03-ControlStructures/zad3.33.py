def dec_to_bin(dec):
    remainder = dec%2
    dec = int(dec/2)
    if dec == 0:
        return str(remainder)
    return dec_to_bin(dec)+str(remainder)

print(dec_to_bin(12))