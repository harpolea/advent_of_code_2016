import numpy as np
import re

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
            print(data, '\n')
            decompressed_file_len += j * len(data)
            counter += i
        else:
            decompressed_file_len += 1
            counter += 1

    print('Length of decompressed file is {}'.format(decompressed_file_len))


if __name__ == "__main__":
    decompress('day9_input.txt')
