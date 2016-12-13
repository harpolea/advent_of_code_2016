import re

def execute(in_file, c_init=0):
    registers = {'a':0, 'b':0, 'c':c_init, 'd':0}

    # read file
    f = open(in_file, 'r')
    lines = f.readlines()

    line_counter = 0

    while(line_counter < len(lines)):
        l = lines[line_counter].replace('\n', '')
        m = re.search('cpy (\d+) ([abcd])', l)
        n =  re.search('cpy ([abcd]) ([abcd])', l)
        if m is not None:
            registers[m.group(2)] =  int(m.group(1))
            line_counter += 1
        elif n is not None:
            registers[n.group(2)] = registers[n.group(1)]
            line_counter += 1
        elif 'inc' in l:
            registers[l[-1]] += 1
            line_counter += 1
        elif 'dec' in l:
            registers[l[-1]] -= 1
            line_counter += 1
        else:
            m = re.search('jnz (\S+) (\d+)', l)
            if m is None:
                m = re.search('jnz (\S+) (-\d+)', l)
            r = m.group(1)
            if (r in 'abcd' and not(registers[r] == 0)):
                line_counter += int(m.group(2))
            elif r.isnumeric() and not(int(r) == 0):
                line_counter += int(m.group(2))
            else:
                line_counter += 1

    print('Register a contains {}'.format(registers['a']))

if __name__ == "__main__":
    print('Part 1:')
    execute('day12_input.txt')
    print('Part 2:')
    execute('day12_input.txt', c_init=1)
