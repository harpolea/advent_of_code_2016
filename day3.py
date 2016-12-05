import numpy as np

def find_triangles_part_1(in_file):
    # read file
    f = open(in_file, 'r')
    lines = []
    for l in f:
        l = l.replace('\n', '')
        lines.append(l)
    # remove last blank one
    if lines[-1] == '':
        lines = lines[:-1]
    lines = np.array(lines)
    possible_total = 0 # total number of possible triangles

    for l in lines:
        lengths = l.split()
        lengths = [int(i) for i in lengths]
        lengths = sorted(lengths)
        if (lengths[0] + lengths[1]) > lengths[2]:
            possible_total += 1

    print('Found {} possible triangles out of {}.'.format(possible_total, len(lines)))

def find_triangles_part_2(in_file):
    # read file
    f = open(in_file, 'r')
    lines = []
    for l in f:
        l = l.replace('\n', '')
        l = l.split()
        l = [int(i) for i in l]
        lines.append(l)
    # remove last blank one
    if lines[-1] == '':
        lines = lines[:-1]

    lines = np.array(lines)
    rot_lines = np.zeros_like(lines)
    # now rotate
    for i in range(int(len(lines) / 3)):
        rot_lines[i*3,:] = sorted(lines[i*3:(i+1)*3,0])
        rot_lines[i*3+1,:] = sorted(lines[i*3:(i+1)*3,1])
        rot_lines[i*3+2,:] = sorted(lines[i*3:(i+1)*3,2])

    possible_total = 0 # total number of possible triangles

    for l in rot_lines:
        if (l[0] + l[1]) > l[2]:
            possible_total += 1

    print('Found {} possible triangles out of {}.'.format(possible_total, len(lines)))

if __name__ == "__main__":
    find_triangles_part_2('day3_input.txt')
