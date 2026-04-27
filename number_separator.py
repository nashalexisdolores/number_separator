import os

class NumberProcessor:
    def __init__(self, input_file="numbers.txt"):
        self.input_file = input_file

    def split_even_odd(self):
        if not os.path.exists(self.input_file):
            print("Error: Input file not found.")
            return