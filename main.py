from hamming_codes import hamming_encode, hamming_decode
from cyclic_codes import crc_encode, crc_check
from compression import HuffmanCoding
from crypto import xor_encrypt, xor_decrypt

def demo():
    message = "HELLO"
    print("Original Message:", message)

    # Compression
    huff = HuffmanCoding()
    encoded, huff_dict = huff.encode(message)
    print("Huffman Encoded:", encoded)

    # Hamming(7,4) Error Correction
    data_bits = "1011"
    encoded_hamming = hamming_encode(data_bits)
    print("Hamming Encoded:", encoded_hamming)

    # Introduce error
    encoded_hamming[2] ^= 1
    print("Received with Error:", encoded_hamming)
    decoded_hamming = hamming_decode(encoded_hamming)
    print("Corrected Data:", decoded_hamming)

    # CRC
    data = "1101"
    crc_code = crc_encode(data, "1011")
    print("CRC Encoded:", crc_code, "Valid?", crc_check(crc_code))

    # Encryption
    cipher = xor_encrypt([int(b) for b in encoded])
    print("Encrypted Huffman Bits:", cipher)
    plain = xor_decrypt(cipher)
    print("Decrypted:", plain)

if __name__ == "__main__":
    demo()
