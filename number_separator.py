import os

class NumberProcessor:
    def __init__(self, input_file="numbers.txt"):
        self.input_file = input_file

    def split_even_odd(self):
        if not os.path.exists(self.input_file):
            print("Error: Input file not found.")
            return
        
        with open(self.input_file, 'r') as src, \
             open('even.txt', 'w') as ev, \
             open('odd.txt', 'w') as od:
            for line in src:
                num = int(line.strip())
                if num % 2 == 0:
                    ev.write(f"{num}\n")
                else:
                    od.write(f"{num}\n")