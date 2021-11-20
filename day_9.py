from aocd import get_data
import numpy as np

input_data = get_data(year=2020, day=9)
test_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def process_data(input_data):
    data = np.array([int(i) for i in input_data.split('\n')])
    return data

def check_preamble(preamble, target):
    return target in np.add.outer(preamble, preamble)

def find_answer(input_data, preamble_length):
    data = process_data(input_data)
    for i in range(preamble_length, data.shape[0]):
        preamble = data[(i-preamble_length):i]
        target = data[i]
        if not check_preamble(preamble, target):
            print(target)

def find_answer_part_two(input_data, target):
    data = process_data(input_data)
    for i in range(data.shape[0]):
        check_sum = 0
        j = 0
        while check_sum < target:
            check_sum += data[i+j]
            if check_sum == target:
                rng = data[i:i+j+1]
                weakness = np.min(rng)+np.max(rng)
                print(weakness)
                return
            j += 1

# find_answer(test_data, 5)
# find_answer_part_two(test_data, target=127)

find_answer(input_data, 25)
find_answer_part_two(input_data, target=248131121)