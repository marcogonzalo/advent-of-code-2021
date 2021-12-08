import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import *


def calc_last_position(course):
    aim = 0
    depth = 0
    horizontal_pos = 0
    for c in course:
        command, value = c.split(' ')
        units = int(value)
        if command == 'up':
            aim -= units 
        elif command == 'down':
            aim += units 
        elif command == 'forward':
            horizontal_pos += units 
            depth += units * aim
        else:
            continue
    return horizontal_pos, depth


def multiply_last_position(course):
    horizontal_pos, depth = calc_last_position(course)
    return horizontal_pos * depth


def main():
    file_path = os.path.dirname(__file__)  + '/input.txt'
    values = get_input_array(filename=file_path)
    position_product = multiply_last_position(values)
    print("Last position value: {}".format(position_product))


main()
