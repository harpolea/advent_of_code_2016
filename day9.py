import numpy as np
import re

def decompressed_len(t):
    m = re.search('\((\d+)x(\d+)\)', t)
    if m is None:
        return len(t)
    else:
        i = int(m.group(1))
        j = int(m.group(2))

        return len(t[:t.index('(')]) + j * decompressed_len(t[t.index(')')+1:t.index(')')+1+i]) + decompressed_len(t[t.index(')')+1+i:])

def decompress(in_file):
    # read file
    f = open(in_file, 'r')

    text = f.read()
    text = re.sub('[ \n]', '', text)
    counter = 0
    decompressed_file_len = 0

    while counter < len(text):
        l = text[counter]
        if l == '(':
            m = re.search('(\d+)x(\d+)', text[counter+1:counter+10])
            i = m.group(1)
            j = m.group(2)
            counter += 3 + len(i) + len(j)
            i = int(i)
            j = int(j)
            data = text[counter:counter+i]
            decompressed_file_len += j * len(data)
            counter += i
        else:
            decompressed_file_len += 1
            counter += 1

    print('Length of decompressed file is {}'.format(decompressed_file_len))

    print('Length of decompressed file in format 2 is {}'.format(decompressed_len(text)))


if __name__ == "__main__":
    decompress('day9_input.txt')
