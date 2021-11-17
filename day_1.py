from aocd import get_data

input_data = get_data(year=2020, day=1)

def process_data(input_data):
    data = [int(i) for i in input_data.split('\n')]
    return data

def find_entries(data):
    for i, val_i in enumerate(data):
        for j, val_j in enumerate(data):
            if i != j and val_i + val_j == 2020:
                return i, j

def find_three_entries(data):
    for i, val_i in enumerate(data):
        for j, val_j in enumerate(data):
            for k, val_k in enumerate(data):
                if i != j and j != k and i != k and val_i + val_j + val_k == 2020:
                    return i, j, k

def find_answer(input_data):
    data = process_data(input_data)
    i, j = find_entries(data)
    print(data[i]*data[j])

def find_answer_part_two(input_data):
    data = process_data(input_data)
    i, j, k = find_three_entries(data)
    print(data[i]*data[j]*data[k])

find_answer(input_data)
find_answer_part_two(input_data)
