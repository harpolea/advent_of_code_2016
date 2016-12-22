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

    n_viable = 0

    for i, n in enumerate(nodes):
        for m in nodes[i+1:]:
            if (n.used > 0 and n.used < m.avail) or (m.used > 0 and m.used < n.avail):
                n_viable += 1
    print('There are {} viable nodes.'.format(n_viable))

    return


if __name__ == "__main__":
    nodes('day22_input.txt')
