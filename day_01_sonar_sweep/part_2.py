import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import *


def count_measurement_increments(measurements, window_size=3):
    measuremnts_count = len(measurements)
    if measuremnts_count <= window_size:
        return 0 
    
    counter = 0
    previous_sum = sum(measurements[0:window_size])
    for m in range(window_size, measuremnts_count):
        current_sum = previous_sum - measurements[m - window_size] + measurements[m]
        if current_sum > previous_sum:
            counter = counter + 1 
        previous_sum = current_sum
    return counter

def main():
    file_path = os.path.dirname(__file__)  + '/input.txt'
    values = get_input_array(filename=file_path, parse_as='integer')
    total_increments = count_measurement_increments(values)
    print("Total increments: {}".format(total_increments))

main()
