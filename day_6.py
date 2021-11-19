from aocd import get_data
from collections import Counter

input_data = get_data(year=2020, day=6)
test_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def process_entry(raw):
    people_count = len(raw.split('\n'))
    processed = raw.replace('\n','')
    return processed, people_count

def process_data(input_data):
    all_entries = input_data.split('\n\n')
    processed_groups = []
    for raw in all_entries:
        processed, people_count = process_entry(raw)
        processed_groups.append([processed, people_count])
    return processed_groups

def find_answer(input_data):
    processed_groups = process_data(input_data)
    answer = 0
    for group, people_count in processed_groups:
        c = Counter([c for c in group])
        answer += len(list(c))
    print(answer)


def find_answer_part_two(input_data):
    processed_groups = process_data(input_data)
    answer = 0
    for group, people_count in processed_groups:
        c = Counter(group)
        for elem, cnt in c.items():
            if cnt == people_count:
                answer += 1
    print(answer)

find_answer(input_data)
# find_answer(test_data)
# find_answer_part_two(test_data)
find_answer_part_two(input_data)