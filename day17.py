import hashlib

def path(passcode):

    routes = [[(0,0), '']]

    def hash_me(a):
        return str(hashlib.md5(str.encode(a)).hexdigest())[:4]

    def open_doors(h):
        doors = ''
        ds = ['U', 'D', 'L', 'R']
        for i in range(4):
            if h[i] in 'bcdef':
                doors += ds[i]
        return doors

    found_vault = False

    longest_path = 0

    while len(routes) > 0:
        new_routes = []
        for r in routes:
            pos = r[0]
            doors = open_doors(hash_me(passcode + r[1]))
            for d in doors:
                new_pos = pos
                new_route = r[1]
                if d == 'D' and (pos[1] + 1 < 4):
                    new_pos = (pos[0], pos[1] + 1)
                    new_route += 'D'
                    new_routes.append([new_pos, new_route])
                elif d == 'U' and pos[1] - 1 >= 0:
                    new_pos = (pos[0], pos[1] - 1)
                    new_route += 'U'
                    new_routes.append([new_pos, new_route])
                elif d == 'L' and pos[0] - 1 >= 0:
                    new_pos = (pos[0] -1, pos[1])
                    new_route += 'L'
                    new_routes.append([new_pos, new_route])
                elif d == 'R' and pos[0] + 1 < 4:
                    new_pos = (pos[0] + 1, pos[1])
                    new_route += 'R'
                    new_routes.append([new_pos, new_route])
                if new_pos == (3,3):
                    found_vault = True
                    #print('Found vault! Path is {} and has length {}'.format(new_route, len(new_route)))
                    new_routes = new_routes[:-1]
                    longest_path = len(new_route)

        routes = new_routes
        if len(routes) == 0:
            print('No longer possible to reach vault :(')
            found_vault = True

    print('Longest route to vault is: {}'.format(longest_path))

if __name__ == "__main__":
    in_str = "ulqzkmiv"
    path(in_str)
