from aocd import get_data

input_data = get_data(year=2020, day=3)

def process_data(input_data):
    data = []
    for i in input_data.split('\n'):
        data.append([c for c in i])
    return data

def rollover(val, max_val):
    new_val = val
    if val >= max_val or val < 0:
        new_val = val % max_val
    return new_val

def check_path(map, right, down):
    row = 0
    col = 0
    max_row = len(map)
    max_col = len(map[0])
    trees = 0
    while row < max_row - down:
        row += down
        col += right
        col = rollover(col, max_col)
        cur_pos = map[row][col]
        if cur_pos == '#':
            trees += 1
    return trees

def find_answer(input_data):
    map = process_data(input_data)
    right = 3
    down = 1
    print(check_path(map, right, down))

def find_answer_part_two(input_data):
    map = process_data(input_data)
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    answer = 1
    for right, down in slopes:
        answer *= check_path(map, right, down)
    print(answer)

find_answer(input_data)
find_answer_part_two(input_data)