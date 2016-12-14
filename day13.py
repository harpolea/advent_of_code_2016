import numpy as np

def open_or_wall(x, y, fav_num=1364):
    binary = '{0:020b}'.format(x**2 + 3*x + 2*x*y + y + y**2 + fav_num)
    total = sum([int(i) for i in binary])
    if total % 2 == 0:
        return True # open
    else:
        return False # wall

def cost_estimate(xy, goal=(31,39)):
    # straight line distance
    return np.sqrt((goal[0]-xy[0])**2 + (goal[1]-xy[1])**2)

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    n_steps = len(total_path) - 1
    print('Path is: {}'.format(total_path))
    print('Path has length {}'.format(n_steps))
    return total_path, n_steps

def tadd(a, b):
    # tuple add
    return (a[0] + b[0], a[1] + b[1])

def neighbours(xy):
    stencil = [(0,1), (1,0), (0,-1), (-1,0)]
    ns = []
    for s in stencil:
        s = tadd(xy, s)
        if s[0] < 0 or s[1] < 0:
            pass
        elif open_or_wall(s[0], s[1]):
            ns.append(s)
    return ns

def a_star(start=(1,1), goal=(31,39)):
    closedSet = set()
    openSet = {start}
    cameFrom = {}

    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[cost_estimate(start, goal)] = start

    ns = []

    while not (not openSet):
        current = None
        for i in iter(fScore.values()):
            if i in openSet:
                current = i
                break

        # if current is None, choose something in openSet
        current = next(iter(openSet))

        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        # make neighbours
        ns = neighbours(current)

        for n in ns:
            if n in closedSet:
                continue
            tentative_gScore = gScore[current] + 1 # distance to neighbours always 1
            if n not in openSet:
                openSet.add(n)
            elif tentative_gScore >= gScore[n]:
                continue

            cameFrom[n] = current
            gScore[n] = tentative_gScore
            fScore[gScore[n] + cost_estimate(n, goal)] = n

    return False, 1e6

if __name__ == "__main__":
    path, steps = a_star(start=(1,1), goal=(31,39))

    n_locs = 0

    # Find number of locations can reach in < 50 steps
    # need to check all locations in 35 x 35 square as 50 ~= sqrt(2)*35
    for x in range(35):
        for y in range(35):
            path, steps = a_star((1,1), (x,y))

            if steps <= 50:
                n_locs += 1

    print('Can reach {} locations in at most 50 steps.'.format(n_locs))
