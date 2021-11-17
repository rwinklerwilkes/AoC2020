from aocd import get_data
import re
from collections import Counter

input_data = get_data(year=2020, day=2)

def process_data(input_data):
    data = []
    for i in input_data.split('\n'):
        rule, password = i.split(':')
        data.append([rule,password])
    return data

def process_rule(rule):
    rule_regex = r'([0-9]{1,2})\-([0-9]{1,2}) ([a-z])'
    match = re.match(rule_regex, rule)
    low = int(match.group(1))
    high = int(match.group(2))
    letter = match.group(3)
    return low, high, letter

def validate_password(rule, password):
    low, high, letter = process_rule(rule)
    c = Counter([c for c in password])
    if c[letter] >= low and c[letter] <= high:
        return 1
    else:
        return 0

def validate_password_part_two(rule, password):
    low, high, letter = process_rule(rule)
    first = password[low]==letter
    second = password[high] == letter
    if (first or second) and first!=second:
        return 1
    else:
        return 0

def find_answer(input_data):
    data = process_data(input_data)
    counter = 0
    for rule, password in data:
        counter += validate_password(rule, password)
    print(counter)

def find_answer_part_two(input_data):
    data = process_data(input_data)
    counter = 0
    for rule, password in data:
        counter += validate_password_part_two(rule, password)
    print(counter)

find_answer(input_data)
find_answer_part_two(input_data)
