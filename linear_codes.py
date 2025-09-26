import numpy as np

class LinearCode:
    def __init__(self, G, H):
        self.G = np.array(G)  # Generator matrix
        self.H = np.array(H)  # Parity-check matrix

    def encode(self, message):
        """Encode using G matrix"""
        return np.dot(message, self.G) % 2

    def syndrome(self, received):
        """Compute syndrome using H matrix"""
        return np.dot(received, self.H.T) % 2
