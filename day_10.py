from aocd import get_data
from collections import Counter

input_data = get_data(year=2020, day=10)

test_data_small = """16
10
15
5
1
11
7
19
6
12
4"""

test_data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def process_data(input_data):
    data = sorted([0] + [int(i) for i in input_data.split('\n')])
    data.append(data[-1]+3)
    return data

def find_answer(input_data):
    data = process_data(input_data)
    diff = []
    for i in range(1, len(data)):
        diff.append(data[i]-data[i-1])
    c = Counter(diff)
    print(c[1],c[3],c[1]*c[3])

def find_answer_part_two(input_data):
    data = process_data(input_data)
    num_ways = {data[0]:1}
    for i in range(1, len(data)):
        val = data[i]
        new_number_of_ways = num_ways.get(val-1, 0) + num_ways.get(val-2, 0) + num_ways.get(val-3, 0)
        num_ways[val] = new_number_of_ways
    print(num_ways[max(data)])

# find_answer(input_data)
find_answer_part_two(input_data)
