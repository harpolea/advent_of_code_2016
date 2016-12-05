import numpy as np
import collections

def find_rooms_part_1(in_file):
    # read file
    f = open(in_file, 'r')
    total_sum = 0
    for line in f:
        letters = ''
        checksum = line[-7:-2]
        sec_id = int(line[-11:-8])
        for l in line:
            if l.isalpha():
                letters += l
            elif l == '[':
                break
        commonest = collections.Counter(letters).most_common()
        # find 5 letters for checksum
        test_checksum = ''
        i = 0
        while len(test_checksum) < 5:
            if commonest[i][1] > commonest[i+1][1]:
                test_checksum += commonest[i][0]
                i += 1
            else:
                # make list of all with same count
                l = commonest[i][0]
                j = i+1
                while j < len(commonest) and commonest[i][1] == commonest[j][1]:
                    l += commonest[j][0]
                    j += 1
                l = sorted(l)
                test_checksum += ''.join(l)
                i = j

        #print(letters, commonest, sec_id, checksum)
        #print('Found checksum to be: {}'.format(test_checksum[0:5]))
        if test_checksum[0:5] == checksum:
            total_sum += sec_id

    print("sum of valid room sec_ids: {}".format(total_sum))

def find_rooms_part_2(in_file):
    # read file
    f = open(in_file, 'r')
    total_sum = 0
    for line in f:
        letters = ''
        checksum = line[-7:-2]
        sec_id = int(line[-11:-8])
        # calculate how much to shift by
        shift = sec_id % 26

        for l in line:
            if l.isalpha():
                l = chr((ord(l) - ord('a') + shift) % 26 + ord('a'))
                letters += l
            if l == '-':
                letters += ' '
            elif l == '[':
                break

        print(letters)

        if 'object' in letters:
            print("\n\nNorth pole objects at {}\n\n".format(sec_id))

if __name__ == "__main__":
    find_rooms_part_2('day4_input.txt')
