from aocd import get_data
import re

input_data = get_data(year=2020, day=16)
test_data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

def parse_rule(rule):
    rule_regex = r'^([a-z]{1,}): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)$'
    match_obj = re.match(rule_regex, rule)
    rule_name = match_obj.group(1)
    rule_limits = [[int(match_obj.group(2)), int(match_obj.group(3))], [int(match_obj.group(4)), int(match_obj.group(5))]]
    return rule_name, rule_limits

def parse_ticket(ticket):
    pass