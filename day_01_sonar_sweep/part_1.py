import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import *


def count_measurement_increments(measurements):
    measuremnts_count = len(measurements)
    if measuremnts_count <= 1:
        return 0 

    counter = 0
    for m in range(1,measuremnts_count):
        if measurements[m] > measurements[m-1]:
            counter = counter + 1 
    return counter

def main():
    file_path = os.path.dirname(__file__)  + '/part_1.txt'
    values = get_input_array(filename=file_path, parse_as='integer')
    total_increments = count_measurement_increments(values)
    print("Total increments: {}".format(total_increments))

main()
