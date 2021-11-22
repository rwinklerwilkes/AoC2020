from aocd import get_data
from functools import reduce
import numpy as np

input_data = get_data(year=2020, day=13)

test_data = """939
7,13,x,x,59,x,31,19"""

def process_data(input_data):
    start_time, bus_raw = input_data.split('\n')
    start_time = int(start_time)
    buses = []
    for b in bus_raw.split(','):
        if b!='x':
            buses.append(int(b))
    return start_time, buses

def check_buses(start_time, buses):
    i = start_time
    found = False
    while not found:
        chk = [i%bus==0 for bus in buses]
        zero = np.where(chk)[0]
        if zero.shape[0]:
            bus = buses[zero[0]]
            time = i
            print(bus*(time-start_time))
            found = True
        i+=1

#Code shamelessly stolen from https://medium.com/analytics-vidhya/chinese-remainder-theorem-using-python-25f051e391fc
def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc * b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def find_answer(input_data):
    start_time, buses = process_data(input_data)
    check_buses(start_time, buses)

def process_data_part_two(input_data):
    start_time, bus_raw = input_data.split('\n')
    start_time = int(start_time)
    buses = []
    for i, b in enumerate(bus_raw.split(',')):
        if b!='x':
            buses.append((int(b),i))
    return start_time, buses

def find_answer_part_two(input_data):
    start_time, buses = process_data_part_two(input_data)
    answer = chinese_remainder([bus[0] for bus in buses], [-bus[1] for bus in buses])
    print(answer)


# find_answer_part_two(test_data)
find_answer_part_two(input_data)