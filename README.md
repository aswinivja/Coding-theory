# Mathematical Coding Theory

###  Overview  
This project demonstrates core concepts of **Mathematical Coding Theory** applied to **data compression, error detection, error correction, and cryptography**.  
It is designed as a modular Python package where each coding theory concept is implemented in its own module, with a `main.py` (and corresponding notebook) to showcase an **end-to-end data transmission simulation**.  

---

###  Features  
 **Linear Codes** – Generator & Parity-check matrices  
 **Cyclic Codes** – CRC encoding & checking using polynomials  
 **Error-Correcting Codes** – Hamming(7,4) with single-bit error correction  
 **Data Compression** – Huffman coding for text compression  
 **Cryptography** – Simple XOR-based encryption & decryption  
 **Demo Application** – Complete pipeline:  
`Message → Compression → Encoding → Encryption → Noise (Errors) → Decryption → Decoding → Decompression → Recovered Message`  

---

###  Project Structure
```
coding_theory_project/
│── linear_codes.py        # Linear codes (G, H matrices)
│── cyclic_codes.py        # Cyclic codes (CRC encoding/validation)
│── hamming_codes.py       # Hamming(7,4) error correction
│── compression.py         # Huffman compression/decompression
│── crypto.py              # Simple XOR cipher
│── main.py                # Demo pipeline
│── *.ipynb                # Jupyter notebooks for each module
```

---

###  Example Output  
```
Original Message: HELLO
Huffman Encoded: 0100110110
Hamming Encoded: [1, 0, 1, 1, 0, 1, 1]
Received with Error: [1, 0, 0, 1, 0, 1, 1]
Corrected Data: [1, 0, 1, 1]
CRC Encoded: [1, 1, 0, 1, 0, 1, 1] Valid? True
Encrypted Huffman Bits: [1, 0, 0, 1, 1, 0, 1, 0]
Decrypted: [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
```

---

###  Applications  
- **Error detection & correction** in communication systems  
- **Efficient storage & transmission** using compression  
- **Secure communication** combining cryptography with coding theory  
- **Educational tool** for students learning coding theory concepts  
