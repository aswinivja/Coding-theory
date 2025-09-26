def xor_encrypt(data, key="1010"):
    key = list(map(int, key))
    return [(int(bit) ^ key[i % len(key)]) for i, bit in enumerate(data)]

def xor_decrypt(data, key="1010"):
    return xor_encrypt(data, key)  # same as encryption
