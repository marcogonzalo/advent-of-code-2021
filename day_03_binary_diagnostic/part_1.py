import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import *
from collections import defaultdict

def calc_rates(diagnostic_report):
    row_len = len(diagnostic_report[0])
    total_rows = len(diagnostic_report)
    min_for_common = total_rows / 2
    ones_qty = [0 for i in range(row_len)]

    for row in diagnostic_report:
        for bit in range(row_len):
            ones_qty[bit] += 1 if row[bit] != '0' else 0

    gamma_rate = '0b'
    for qty in ones_qty:
        gamma_rate += '1' if qty > min_for_common else '0'

    epsilon_rate = bin(int(gamma_rate, 2) ^ int('1' * row_len, 2))
    return int(gamma_rate, 2), int(epsilon_rate, 2)


def calc_power_consumption(diagnostic_report):
    gamma_rate, epsilon_rate = calc_rates(diagnostic_report)
    return epsilon_rate * gamma_rate


def main():
    file_path = os.path.dirname(__file__)  + '/input.txt'
    values = get_input_array(filename=file_path)
    power_consumption = calc_power_consumption(values)
    print("Submarine power consumption: {}".format(power_consumption))


main()
