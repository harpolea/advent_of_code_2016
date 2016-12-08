import numpy as np
import re

def pixels(in_file):
    screen = np.zeros((6, 50), dtype=bool)

    def rect(a,b):
        screen[:b,:a] = True

    def rot_row(a, b):
        row = screen[a, :].copy()
        screen[a, b:] = row[:-b]
        screen[a, :b] = row[-b:]

    def rot_col(a, b):
        col = screen[:, a].copy()
        screen[b:, a] = col[:-b]
        screen[:b, a] = col[-b:]

    # read file
    f = open(in_file, 'r')

    for line in f:
        line = line.replace('\n', '')
        m = re.search('rect (\d+)x(\d+)', line)
        if m is not None:
            rect(int(m.group(1)), int(m.group(2)))
        m = re.search('rotate row y=(\d+) by (\d+)', line)
        if m is not None:
            rot_row(int(m.group(1)), int(m.group(2)))
        m = re.search('rotate column x=(\d+) by (\d+)', line)
        if m is not None:
            rot_col(int(m.group(1)), int(m.group(2)))

    print("There are {} pixels lit.".format(sum(sum(screen))))
    screen = np.int_(screen)
    print(screen[:,:24], '\n')
    print(screen[:,24:])

if __name__ == "__main__":
    pixels('day8_input.txt')
