from aocd import get_data
import re

input_data = get_data(year=2020, day=8)
test_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class Program:
    def __init__(self):
        self.cur_location = 0
        self.accumulator = 0
        self.repeated = False
        self.instructions = []
        self.instructions_backup = []
        self.times_visited = []

    def reset_program(self):
        self.times_visited = [0 for i in range(len(self.times_visited))]
        self.accumulator = 0
        self.cur_location = 0
        self.repeated = False
        self.instructions = self.instructions_backup.copy()

    def process_input(self, raw_input):
        lines = raw_input.split('\n')
        for line in lines:
            spl = line.split(' ')
            instruction = spl[0]
            val = spl[1]
            if val[0] == '+':
                val = int(val[1:])
            else:
                val = -int(val[1:])
            self.instructions.append((instruction, val))
            self.times_visited.append(0)
        self.instructions_backup = self.instructions.copy()

    def process_instruction(self, instruction, value):
        if instruction == 'acc':
            self.accumulator += value
            self.cur_location += 1
        elif instruction == 'jmp':
            self.cur_location += value
        elif instruction == 'nop':
            self.cur_location += 1


    def run_program(self, inst_to_change=None):
        self.reset_program()
        if inst_to_change:
            # print(f'Changing {inst_to_change}')
            cur_inst = self.instructions[inst_to_change]
            if cur_inst[0] == 'nop':
                self.instructions[inst_to_change] = ('jmp',cur_inst[1])
            elif cur_inst[0] == 'jmp':
                self.instructions[inst_to_change] = ('nop',cur_inst[1])

        while not self.repeated:
            if self.cur_location < 0 or self.cur_location > len(self.instructions):
                self.repeated = True
            elif self.cur_location == len(self.instructions):
                break
            elif self.times_visited[self.cur_location] == 1:
                self.repeated = True
                print(self.accumulator)
            self.times_visited[self.cur_location] += 1
            inst, val = self.instructions[self.cur_location]
            # print(inst, val)
            self.process_instruction(inst, val)

        if not self.repeated:
            print('LAST INSTRUCTION', self.accumulator)
            self.repeated = False

        return self.repeated



    def run_program_with_modifications(self):
        for i, (inst, val) in enumerate(self.instructions):
            if inst in ['nop', 'jmp']:
                repeated = self.run_program(i)
                if not repeated:
                    break

p = Program()
p.process_input(input_data)
p.run_program()

p = Program()
p.process_input(input_data)
p.run_program_with_modifications()