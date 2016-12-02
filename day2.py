import numpy as np

def find_code(in_file):
    f = open(in_file, 'r')
    lines = []
    for l in f:
        l = l.replace('\n', '')
        lines.append(l)
    # remove last blank one
    if lines[-1] == '':
        lines = lines[:-1]

    #keypad = np.array([[1,2,3], [4,5,6], [7,8,9]])
    keypad = np.array([['x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', '1', 'x', 'x', 'x'], ['x', 'x', '2', '3', '4', 'x', 'x'], ['x', '5', '6', '7', '8', '9', 'x'], ['x', 'x', 'A', 'B', 'C', 'x', 'x'], ['x', 'x', 'x', 'D', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x']])
    keypad = keypad.transpose()

    def new_pos(p, dir):
        new_p = p.copy()
        if d == "U":
            new_p[1] -= 1
        elif d == "L":
            new_p[0] -= 1
        elif d == "D":
            new_p[1] += 1
        elif d == "R":
            new_p[0] += 1

        if keypad[new_p[0], new_p[1]] == 'x':
            return p
        else:
            return new_p

    pos = np.array([1,3]) # position

    code = ''

    for l in lines:
        for d in l:
            pos = new_pos(pos, d)

        code += str(keypad[pos[0], pos[1]])

    print(code)

if __name__ == "__main__":
    find_code('day2_input.txt')
