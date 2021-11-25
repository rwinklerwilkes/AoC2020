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
    rule_regex = r'^([a-z\s]{1,}): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)$'
    match_obj = re.match(rule_regex, rule)
    rule_name = match_obj.group(1)
    rule_limits = [[int(match_obj.group(2)), int(match_obj.group(3))], [int(match_obj.group(4)), int(match_obj.group(5))]]
    return rule_name, rule_limits

def parse_all_rules(rules):
    rule_demarcations = {}
    for rule_name, rule_limits in rules:
        for lower_limit, upper_limit in rule_limits:
            for i in range(lower_limit, upper_limit + 1):
                rules_at_this_location = rule_demarcations.get(i,[])
                rules_at_this_location.append(rule_name)
                rule_demarcations[i] = rules_at_this_location
    return rule_demarcations

def parse_input_data(input_data):
    sections = input_data.split('\n\n')
    rules = sections[0].split('\n')
    your_ticket = parse_ticket(sections[1].split('\n')[1])
    other_tickets = [parse_ticket(ticket) for ticket in sections[2].split('\n')[1:]]
    all_rules = [parse_rule(rule) for rule in rules]
    all_rules = parse_all_rules(all_rules)
    return all_rules, your_ticket, other_tickets

def check_ticket(ticket, all_rules):
    invalid_values = []
    for value in ticket:
        if len(all_rules.get(value,[])) == 0:
            invalid_values.append(value)
    is_valid = len(invalid_values) == 0
    return is_valid, invalid_values

def find_answer_part_one(input_data):
    all_rules, your_ticket, other_tickets = parse_input_data(input_data)
    invalid_rules = []
    for ticket in other_tickets:
        is_valid, invalid_rules_this_ticket = check_ticket(ticket, all_rules)
        invalid_rules += invalid_rules_this_ticket
    print(sum(invalid_rules))

def find_answer_part_two():
    pass

def parse_ticket(ticket):
    return [int(i) for i in ticket.split(',')]

find_answer_part_one(input_data)