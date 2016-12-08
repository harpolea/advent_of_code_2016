import numpy as np

def test_abba(s):
    if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        return True
    else:
        return False

def test_aba(s):
    if s[0] == s[2] and s[0] != s[1]:
        return True
    else:
        return False

def make_bab(s):
    return s[1] + s[0] + s[1]

def find_ips_part_1(in_file):
    # read file
    f = open(in_file, 'r')

    num_ips = 0

    for line in f:
        line = line.replace('\n', '')

        substr = ''
        hypernet = False
        valid = False

        for l in line:
            if l == '[':
                hypernet = True
                substr = ''
            elif l == ']':
                hypernet = False
                substr = ''
            elif len(substr) < 4:
                substr += l
            if len(substr) == 4:
                abba = test_abba(substr)
                if abba and not hypernet:
                    valid = True
                elif abba and hypernet:
                    valid = False
                    break
                substr = substr[1:]

        if valid:
            print('address {} is valid'.format(line))
            num_ips += 1

    print('Found {} valid ips'.format(num_ips))

def find_ips_part_2(in_file):
    # read file
    f = open(in_file, 'r')

    num_ips = 0

    for line in f:
        line = line.replace('\n', '')

        substr = ''
        hypernet = False
        valid = False

        babs = []
        hypernet_str =  ''

        for l in line:
            if l == '[':
                hypernet = True
                substr = ''
            elif l == ']':
                hypernet = False
            elif hypernet:
                hypernet_str += l
            elif len(substr) < 3:
                substr += l
            if not hypernet and len(substr) == 3:
                if test_aba(substr):
                    babs.append(make_bab(substr))
                substr = substr[1:]

        # now test to see if babs are in hypernet_str
        for b in babs:
            if b in hypernet_str:
                valid = True
                break

        if valid:
            print('address {} is valid'.format(line))
            num_ips += 1

    print('Found {} valid ips'.format(num_ips))


if __name__ == "__main__":
    find_ips_part_2('day7_input.txt')
