from aocd import get_data
import re

input_data = get_data(year=2020, day=14)
test_data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

def int_to_bin(n, zero_pad=36):
    bin_val = ('0'*zero_pad + str(bin(n))[2:])[-36:]
    return bin_val

def bin_to_int(n):
    int_val = int(n,2)
    return int_val

class Program:
    def __init__(self):
        self.memory = {}

    def set_mask(self, mask):
        self.mask = mask

    def mask_int(self, n):
        bn = int_to_bin(n)
        new_str = ''
        for i, val in enumerate(bn):
            if self.mask[i] != 'X':
                new_str += self.mask[i]
            else:
                new_str += val
        new_n = bin_to_int(new_str)
        return new_n

    def set_memory(self, loc, n):
        self.memory[loc] = self.mask_int(n)

    def process_instruction(self, instruction):
        inst_regex = r'^mem\[([0-9]{1,})\] = ([0-9]{1,}$)'
        match_obj = re.match(inst_regex, instruction)
        mem_val = int(match_obj.group(1))
        int_val = int(match_obj.group(2))
        self.set_memory(mem_val, int_val)

    def process_program(self, raw_input_data):
        for instruction in raw_input_data.split('\n'):
            if instruction[:4] == 'mask':
                self.set_mask(instruction[7:])
            else:
                self.process_instruction(instruction)

        final_answer = sum(self.memory.values())
        print(final_answer)

p = Program()
p.process_program(input_data)