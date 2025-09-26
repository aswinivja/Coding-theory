def crc_encode(data, generator="1011"):
    """Cyclic Redundancy Check (CRC) Encoding"""
    data = list(map(int, data))
    gen = list(map(int, generator))
    padded = data + [0] * (len(gen)-1)

    for i in range(len(data)):
        if padded[i] == 1:
            for j in range(len(gen)):
                padded[i+j] ^= gen[j]

    remainder = padded[-(len(gen)-1):]
    return data + remainder

def crc_check(codeword, generator="1011"):
    """Check CRC validity"""
    gen = list(map(int, generator))
    padded = codeword.copy()

    for i in range(len(codeword) - len(gen) + 1):
        if padded[i] == 1:
            for j in range(len(gen)):
                padded[i+j] ^= gen[j]
    return all(bit == 0 for bit in padded[-(len(gen)-1):])
