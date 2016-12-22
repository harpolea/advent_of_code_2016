import re

class Node():
    def __init__(self, x, y, size, used, avail, use):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use

def nodes(in_file):

    # read file
    f = open(in_file, 'r')
    ls = f.readlines()
    nodes = []

    max_x = 0
    max_y = 0

    for l in ls:
        m = re.match('/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', l)
        if m is not None:
            x = int(m.group(1))
            y = int(m.group(2))
            size = int(m.group(3))
            used = int(m.group(4))
            avail = int(m.group(5))
            use = int(m.group(1))

            nodes.append(Node(x, y, size, used, avail, use))
            if x > max_x: max_x = x
            if y > max_y: max_y = y

    n_viable = 0

    for i, n in enumerate(nodes):
        for m in nodes[i+1:]:
            if (n.used > 0 and n.used < m.avail) or (m.used > 0 and m.used < n.avail):
                n_viable += 1
    print('There are {} viable nodes.'.format(n_viable))

    # put node data into grid
    grid = [['.' for i in range(max_x+1)] for j in range(max_y+1)] # index [y][x]
    for n in nodes:
        if n.used / n.size > 0.9:
            grid[n.y][n.x] = '#'
        elif n.used == 0:
            grid[n.y][n.x] = '_'
        if n.y == 0 and n.x == max_x:
            grid[n.y][n.x] = 'G'

    grid[0][0] = 'x'

    for r in grid:
        print(' '.join(r))

    return


if __name__ == "__main__":
    nodes('day22_input.txt')
