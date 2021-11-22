from aocd import get_data
import numpy as np

input_data = get_data(year=2020, day=12)
test_data = """F10
N3
F7
R90
F11"""


class Ship:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.facing = 0

    def determine_facing(self):
        facing_rad = self.facing * np.pi / 180
        facing_x = round(np.cos(facing_rad), 2)
        facing_y = round(np.sin(facing_rad), 2)
        return facing_x, facing_y

    def process_instruction(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            self.pos_y += value
        elif action == 'E':
            self.pos_x += value
        elif action == 'S':
            self.pos_y -= value
        elif action == 'W':
            self.pos_x -= value
        elif action == 'L':
            self.facing += value
            self.facing %= 360
        elif action == 'R':
            self.facing -= value
            self.facing %= 360
        elif action == 'F':
            fx, fy = self.determine_facing()
            self.pos_x += fx * value
            self.pos_y += fy * value

    def get_distance(self):
        return abs(self.pos_x) + abs(self.pos_y)

    def process_instruction_list(self, raw_input):
        instruction_list = raw_input.split('\n')
        for instruction in instruction_list:
            self.process_instruction(instruction)
        print(self.get_distance())


class Ship_Two(Ship):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def rotate_waypoint(self, degree):
        degree_rad = degree * np.pi / 180
        new_x = np.round(self.waypoint_x * np.cos(degree_rad) - self.waypoint_y * np.sin(degree_rad),2)
        new_y = np.round(self.waypoint_x * np.sin(degree_rad) + self.waypoint_y * np.cos(degree_rad),2)
        self.waypoint_x = new_x
        self.waypoint_y = new_y
        return new_x, new_y

    def process_instruction(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            self.waypoint_y += value
        elif action == 'E':
            self.waypoint_x += value
        elif action == 'S':
            self.waypoint_y -= value
        elif action == 'W':
            self.waypoint_x -= value
        elif action == 'L':
            new_x, new_y = self.rotate_waypoint(value)
        elif action == 'R':
            new_x, new_y = self.rotate_waypoint(-value)
        elif action == 'F':
            self.pos_x += self.waypoint_x * value
            self.pos_y += self.waypoint_y * value


# s = Ship()
# s.process_instruction_list(input_data)

s = Ship_Two()
s.process_instruction_list(input_data)