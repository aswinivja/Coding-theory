def hamming_encode(data):
    """Encode 4-bit data into Hamming(7,4)"""
    d = list(map(int, data))
    p1 = (d[0] + d[1] + d[3]) % 2
    p2 = (d[0] + d[2] + d[3]) % 2
    p3 = (d[1] + d[2] + d[3]) % 2
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]

def hamming_decode(code):
    """Decode Hamming(7,4) and correct single-bit errors"""
    p1 = (code[0] + code[2] + code[4] + code[6]) % 2
    p2 = (code[1] + code[2] + code[5] + code[6]) % 2
    p3 = (code[3] + code[4] + code[5] + code[6]) % 2
    error_pos = p1*1 + p2*2 + p3*4

    if error_pos != 0:
        code[error_pos-1] ^= 1  # Correct error

    return [code[2], code[4], code[5], code[6]]
