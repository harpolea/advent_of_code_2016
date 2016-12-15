import re
import numpy as np

def find_time(in_file, part_2=False):
    # read file
    f = open(in_file, 'r')
    lines = f.readlines()

    discs = np.zeros((len(lines), 2))

    for i, line in enumerate(lines):
        m = re.match('Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', line)
        discs[i, :] = [int(m.group(2)), int(m.group(3))]

    if part_2:
        discs = np.append(discs,[[11,0]], axis=0)

    def target(): # calculate target configuration for discs to be in when press button
        return (discs[:,0] - list(range(len(discs))) - 1) % discs[:,0]

    def evolve(): # evolves discs through one timestep
        discs[:,1] = (discs[:,1] + 1) % discs[:,0]

    def compare(l1, l2): # checks equality of lists
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True

    t = 0
    target_config = target()
    while not (compare(discs[:,1],target_config)):
        evolve()
        t+= 1
        if (t%100000 == 0): print(t)

    print('Press the button at t={} for success!'.format(t))

if __name__ == "__main__":
    find_time('day15_input.txt')
    print('Part 2')
    find_time('day15_input.txt', part_2=True)
