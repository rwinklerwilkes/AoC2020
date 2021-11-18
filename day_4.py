from aocd import get_data
import re

input_data = get_data(year=2020, day=4)

test_file = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

test_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

test_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""



def process_entry(raw_entry):
    all_vals = raw_entry.replace('\n', ' ').split(' ')
    split_data = [raw.split(':') for raw in all_vals]
    processed_entry = {raw[0]: raw[1] for raw in split_data}
    return processed_entry


def process_data(input_data):
    all_entries = input_data.split('\n\n')
    processed_entries = [process_entry(raw) for raw in all_entries]
    return processed_entries

def validate_entry(entry, mandatory={'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}, optional={'cid'}):
    keys = set(entry.keys())
    if len(mandatory - keys) == 0:
        present = 1
    else:
        present = 0

    return present

def validate_entry_part_two(entry, validation_rules):
    keys = set(entry.keys())
    mandatory = validation_rules.keys()
    if len(mandatory - keys) == 0:
        valid = 1
        for k in mandatory:
            if not validation_rules[k].is_valid(entry[k]):
                valid = 0
    else:
        valid = 0
    return valid


def find_answer(input_data):
    processed_entries = process_data(input_data)
    answer = sum([validate_entry(entry) for entry in processed_entries])
    print(answer)


def find_answer_part_two(input_data):
    validation = setup_rules()
    processed_entries = process_data(input_data)
    valid = 0
    for entry in processed_entries:
        valid += validate_entry_part_two(entry, validation)
    print(valid)

class PassportField:
    def __init__(self, name):
        self.name = name

    def check_value(self, value_to_check):
        return self.is_valid(value_to_check)

def validation_low_high(value, low, high):
    value = int(value)
    return value >= low and value <= high

def validation_height(height):
    if height[-2:]=='cm':
        return validation_low_high(height[:-2],150,193)
    elif height[-2:]=='in':
        return validation_low_high(height[:-2],59,76)
    else:
        return False

def setup_rules():
    validation = {}
    validation['byr'] = PassportField('byr')
    validation['byr'].is_valid = (lambda x: validation_low_high(x,1920,2002))

    validation['iyr'] = PassportField('iyr')
    validation['iyr'].is_valid = (lambda x: validation_low_high(x,2010,2020))

    validation['eyr'] = PassportField('eyr')
    validation['eyr'].is_valid = (lambda x: validation_low_high(x,2020,2030))

    validation['hgt'] = PassportField('hgt')
    validation['hgt'].is_valid = (lambda x: validation_height(x))

    validation['hcl'] = PassportField('hcl')
    validation['hcl'].is_valid = (lambda x: re.match('#[0-9a-f]{6}',x))

    validation['ecl'] = PassportField('ecl')
    validation['ecl'].is_valid = (lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'])

    validation['pid'] = PassportField('pid')
    validation['pid'].is_valid = (lambda x: re.match('^[0-9]{9}$', x))
    return validation

find_answer(input_data)
find_answer_part_two(input_data)