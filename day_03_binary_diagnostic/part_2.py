import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import *

def calc_rating(diagnostic_report, o2=False):
    row_len = len(diagnostic_report[0])
    checklist = list(diagnostic_report)
    reference = '1' if o2 else '0'
    for bit in range(row_len):
        total_rows = len(checklist)
        if total_rows <= 1:
            break

        ones_counter = 0
        min_for_common = total_rows / 2
        for row in checklist:
            ones_counter += int(row[bit]) 

        if ones_counter >= min_for_common:
            reference = '1' if o2 else '0'
        else:
            reference = '0' if o2 else '1'

        new_checklist = []
        for row in checklist:
            if row[bit] == reference:
                new_checklist.append(row)
        checklist = new_checklist

    return int(checklist[0], 2)


def calc_life_support_rating(diagnostic_report):
    co2_rating = calc_rating(diagnostic_report)
    o2_rating = calc_rating(diagnostic_report, o2=True)
    return co2_rating * o2_rating


def main():
    file_path = os.path.dirname(__file__)  + '/input.txt'
    values = get_input_array(filename=file_path)
    life_support_rating = calc_life_support_rating(values)
    print("Life support rating of the submarine: {}".format(life_support_rating))


main()
