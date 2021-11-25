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

test_data_two = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

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
    rules_with_limits = [parse_rule(rule) for rule in rules]
    all_rules = parse_all_rules(rules_with_limits)
    return all_rules, rules_with_limits, your_ticket, other_tickets

def check_ticket(ticket, all_rules):
    invalid_values = []
    for value in ticket:
        if len(all_rules.get(value,[])) == 0:
            invalid_values.append(value)
    is_valid = len(invalid_values) == 0
    return is_valid, invalid_values

def find_answer_part_one(input_data):
    all_rules, rules_with_limits, your_ticket, other_tickets = parse_input_data(input_data)
    invalid_rules = []
    for ticket in other_tickets:
        is_valid, invalid_rules_this_ticket = check_ticket(ticket, all_rules)
        invalid_rules += invalid_rules_this_ticket
    print(sum(invalid_rules))

def find_answer_part_two(input_data):
    all_rules, rules_with_limits, your_ticket, other_tickets = parse_input_data(input_data)
    valid_tickets = identify_valid_tickets(all_rules, other_tickets)
    rule_locations = identify_rule_locations(all_rules, rules_with_limits, valid_tickets)
    your_rule_values = finalize_your_ticket(your_ticket, rule_locations)
    departure_rules = {rule for rule, limits in rules_with_limits if 'departure' in rule}
    answer = 1
    for rule in departure_rules:
        answer *= your_rule_values[rule]
    print(answer)

def finalize_your_ticket(your_ticket, rule_locations):
    rule_values = {rule:your_ticket[location] for rule,location in rule_locations.items()}
    return rule_values


def identify_valid_tickets(all_rules, other_tickets):
    valid_tickets = []
    for ticket in other_tickets:
        is_valid, invalid_rules_this_ticket = check_ticket(ticket, all_rules)
        if is_valid:
            valid_tickets.append(ticket)
    return valid_tickets


def identify_rule_locations(all_rules, rules_with_limits, valid_tickets):
    rules_only = {rule for rule, limits in rules_with_limits}
    rule_locations = {rule:list(range(len(rules_only))) for rule in rules_only}
    for ticket in valid_tickets:
        for location, value in enumerate(ticket):
            #location is a location on the ticket
            #possible_values is all of the rules which may be applicable at that location
            possible_rules = set(all_rules[value])
            #find all rules which don't apply here and remove this location from them
            for rule in rules_only - possible_rules:
                old_locations = rule_locations[rule]
                rule_locations[rule] = [i for i in old_locations if i != location]

    done = False
    finished_rules = {}
    while not done:
        finished_rules = {k: v[0] for k, v in rule_locations.items() if len(v) == 1}
        finished_locations = {v for k, v in finished_rules.items()}
        #loop over all rules and remove any decided locations
        new_rule_locations = {}
        for rule, locations in rule_locations.items():
            if rule in finished_rules:
                new_rule_locations[rule] = rule_locations[rule]
            else:
                new_rule_locations[rule] = list(set(locations) - finished_locations)
        rule_locations = new_rule_locations
        #check if we're done
        done = len(finished_rules.keys()) == len(rules_only)

    return finished_rules

def parse_ticket(ticket):
    return [int(i) for i in ticket.split(',')]

# find_answer_part_one(input_data)
find_answer_part_two(input_data)