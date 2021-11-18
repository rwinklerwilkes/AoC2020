from aocd import get_data
import math


input_data = get_data(year=2020, day=5)

def process_data(input_data):
    data = input_data.split('\n')
    return data


def calculate_direction(direction_string, lower, upper):
    tmp_lower = lower
    tmp_upper = upper
    for char in direction_string:
        midpoint = (tmp_upper + tmp_lower) / 2
        if char == '0':
            tmp_upper = math.floor(midpoint)
        elif char == '1':
            tmp_lower = math.ceil(midpoint)

    assert tmp_lower == tmp_upper
    return tmp_lower


def process_boarding_pass(boarding_pass):
    front_back = boarding_pass[:7]
    front_back = front_back.replace('F', '0').replace('B', '1')
    left_right = boarding_pass[-3:]
    left_right = left_right.replace('L', '0').replace('R', '1')
    row = calculate_direction(front_back, 0, 127)
    seat = calculate_direction(left_right, 0, 7)
    seat_id = row*8+seat
    return seat_id


def find_answer(input_data):
    data = process_data(input_data)
    max_id = 0
    all_ids = []
    for boarding_pass in data:
        id = process_boarding_pass(boarding_pass)
        all_ids.append(id)
        if id > max_id:
            max_id = id
    print(max_id)
    return all_ids

def find_answer_part_two(input_data):
    all_ids = sorted(find_answer(input_data))
    min_id = all_ids[0]
    max_id = all_ids[-1]
    print(set(range(min_id, max_id+1))-set(all_ids))

_ = find_answer(input_data)
find_answer_part_two(input_data)
