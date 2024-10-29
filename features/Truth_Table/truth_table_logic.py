# This script creates the base Truth Table to track valid and invalid combinations of options based upon predefined rules

import numpy as np

class TruthTable:
    def __init__(self, n=14, x=30, m=30, y=35):
        self.n, self.x, self.m, self.y = n, x, m, y
        self.table = np.zeros((n, x, m, y), dtype=int)

    def update_table(self, n, x, m, y, validity):
        """Update the Truth Table based on the validity of the combination."""
        self.table[n, x, m, y] = validity

    def is_valid_combination(self, n, x, m, y):
        """Check if a specific combination is valid."""
        return self.table[n, x, m, y] == 1
