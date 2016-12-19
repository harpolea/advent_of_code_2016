import re, copy
import numpy as np

def dragon(in_str, target_length):

    def make_data(a):
        b = a[::-1]
        trantab = b.maketrans("01", "10")
        b = b.translate(trantab)
        return a + '0' + b

    while len(in_str) < target_length:
        in_str = make_data(in_str)

    def make_checksum(a):
        c = ''
        for i in range(int(len(a)/2)):
            if a[2*i] == a[2*i+1]:
                c += '1'
            else:
                c += '0'
        return c

    checksum = make_checksum(in_str[:target_length])
    while len(checksum) % 2 != 1:
        checksum = make_checksum(checksum)

    print('Checksum is {}.'.format(checksum))


if __name__ == "__main__":
    in_str = "00101000101111010"
    target_length = 35651584
    dragon(in_str, target_length)
