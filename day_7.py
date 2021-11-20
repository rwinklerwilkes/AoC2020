from aocd import get_data
import re

input_data = get_data(year=2020, day=7)
test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def process_entry(raw):
    no_bags = '^no other bags$'
    number_of_bags = r'^([0-9]{1,}) ([a-z ]{1,}) bag[s]{0,1}$'

    bag_type = r'([a-z ]{1,}) bag[s]'
    bag_split = raw[:-1].split(" contain ")
    color = bag_split[0]
    color_match = re.match(bag_type, color)
    color = color_match.group(1)

    other_bags = {}
    remainder = bag_split[1].split(', ')
    for raw_bag in remainder:
        if re.match(no_bags, raw_bag):
            continue
        else:
            om = re.match(number_of_bags, raw_bag)
            assert om is not None
            number_of_other_bags = om.group(1)
            bag_type = om.group(2)
            other_bags[bag_type] = number_of_other_bags
    return color, other_bags


class Bag:
    def __init__(self, color):
        self.color = color
        self.contains = {}

    def __repr__(self):
        return self.color

    def can_contain(self, other, number):
        self.contains[other] = number

    def eventually_contains(self):
        total = 0
        for bag, number in self.contains.items():
            total += number * (bag.eventually_contains()+1)
        return total


def process_data(input_data):
    all_entries = input_data.split('\n')
    processed_groups = [process_entry(entry) for entry in all_entries]
    bags = {}
    for group in processed_groups:
        color = group[0]
        bags[color] = bags.get(color, Bag(color))
        for other_color, number_of_other_bags in group[1].items():
            other_bag = bags.get(other_color, Bag(other_color))
            bags[other_color] = other_bag
            bags[color].can_contain(other_bag, int(number_of_other_bags))

    contained_by = {}
    for bag in bags.keys():
        bag_obj = bags[bag]
        for other_bag in bag_obj.contains:
            cb = contained_by.get(other_bag, [])
            cb.append(bag_obj)
            contained_by[other_bag] = cb

    return bags, contained_by


def find_bags(contained_by, contains, target_color):
    target_bag = contains[target_color]
    stack = contained_by[target_bag].copy()
    eventually_contained = set()
    already_visited = {}
    while stack:
        cur_bag = stack.pop()
        eventually_contained.add(cur_bag)
        if not already_visited.get(cur_bag, None):
            stack += contained_by.get(cur_bag, [])
        else:
            already_visited[cur_bag] = True
    return eventually_contained


def find_answer(input_data):
    contains, contained_by = process_data(input_data)
    eventually_contained = find_bags(contained_by, contains, 'shiny gold')
    answer = len(eventually_contained)
    print(answer)
    return answer


def find_answer_part_two(input_data):
    contains, contained_by = process_data(input_data)
    answer = contains['shiny gold'].eventually_contains()
    print(answer)
    return answer


# contains, contained_by = process_data(test_data)
answer = find_answer(input_data)
answer = find_answer_part_two(input_data)