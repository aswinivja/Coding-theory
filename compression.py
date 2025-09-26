import heapq
from collections import Counter

class HuffmanCoding:
    def build_tree(self, text):
        freq = Counter(text)
        heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    def encode(self, text):
        huff = self.build_tree(text)
        huff_dict = {a: b for a, b in huff}
        return ''.join(huff_dict[ch] for ch in text), huff_dict

    def decode(self, encoded, huff_dict):
        inv = {v: k for k, v in huff_dict.items()}
        current, decoded = "", ""
        for bit in encoded:
            current += bit
            if current in inv:
                decoded += inv[current]
                current = ""
        return decoded
