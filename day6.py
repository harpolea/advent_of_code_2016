import numpy as np
import collections

def find_code(in_file):
    # read file
    f = open(in_file, 'r')
    lines = []
    for l in f:
        lines.append(list(l[:-1]))
    # now rotate
    lines = np.array(lines).transpose()

    part_1_code = ''
    part_2_code = ''
    for p in lines:
        part_1_code += collections.Counter(p).most_common()[0][0]
        part_2_code += collections.Counter(p).most_common()[-1][0]

    print('Code for part 1 is {}'.format(part_1_code))
    print('Code for part 2 is {}'.format(part_2_code))

if __name__ == "__main__":
    find_code('day6_input.txt')
