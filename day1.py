instructions = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"

instructions = instructions.split(', ')

coord = [0,0]
direction = 0
visited_locations = dict()
visited_locations['x0y0'] = True
endpoint = False

for i in instructions:
    # use modular arithmetic to find direction
    if i[0] == 'L':
        direction -= 1
    else:
        direction += 1

    if direction == -1:
        direction = 3
    if direction == 4:
        direction = 0

    steps = int(i[1:])

    for s in range(steps):
        if direction == 0: # facing north
            coord[1] += 1
        elif direction == 1: # facing east
            coord[0] += 1
        elif direction == 2: # south
            coord[1] -= 1
        else:
            coord[0] -= 1

        # test to see if we've been here before
        key = 'x' + str(coord[0]) + 'y' + str(coord[1])

        if key in visited_locations:
            endpoint = True
            break
        else:
            visited_locations[key] = True
    if endpoint:
        break

print('Final destination: {}, which is {} blocks away'.format(coord, abs(coord[0]) + abs(coord[1])))
