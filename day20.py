import re

def firewall(in_file):
    # read file
    f = open(in_file, 'r')
    ranges = []
    for l in f:
        m = re.match('(\d+)-(\d+)', l)
        ranges.append([int(m.group(1)), int(m.group(2))])

    ranges.sort()
    lowest = 0
    upper_lim = 0
    for r in ranges:
        if lowest < r[0]:
            print('Found lowest-valued unblocked IP: {}'.format(lowest))
            return
        else:
            if r[1] > upper_lim:
                upper_lim = r[1]
            lowest = upper_lim+1

    # all are blocked
    if lowest > 4294967295:
        print('All IPs are blocked :(')
    else:
        print('Found lowest-valued unblocked IP: {}'.format(lowest))
    return

def firewall_part2(in_file):
    # read file
    f = open(in_file, 'r')
    ranges = []
    for l in f:
        m = re.match('(\d+)-(\d+)', l)
        ranges.append([int(m.group(1)), int(m.group(2))])

    ranges.sort()
    lowest = 0
    upper_lim = 0
    n_unblocked = 0
    for r in ranges:
        if lowest < r[0]:
            n_unblocked += r[0] - lowest
        if r[1] > upper_lim:
            upper_lim = r[1]
        lowest = upper_lim+1

    max_IP = 4294967295
    if lowest < max_IP:
        n_unblocked += max_IP+1 - lowest

    print('Found {} unblocked IPs.'.format(n_unblocked))
    return

if __name__ == "__main__":
    firewall('day20_input.txt')
    firewall_part2('day20_input.txt')
