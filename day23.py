import re

def execute(in_file, a_init=7):
    registers = {'a':a_init, 'b':0, 'c':0, 'd':0}

    # read file
    f = open(in_file, 'r')
    lines = f.readlines()

    line_counter = 0

    while (line_counter < len(lines)):
        l = lines[line_counter].replace('\n', '')
        m = re.search('cpy (\d+) ([abcd])', l)
        if m is None:
            m = re.search('cpy (-\d+) ([abcd])', l)
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
        elif 'mul' in l:
            m = re.search('mul (\w) (\w) (\w)', l)
            registers[m.group(3)] = registers[m.group(1)] * registers[m.group(2)]
            line_counter += 1
        elif 'tgl' in l:
            m = re.search('tgl (\w+)', l)
            if m is None:
                m = re.search('tgl (-\w+)', l)
            x = registers[m.group(1)]
            if line_counter + x < len(lines):
                target = lines[line_counter + x]
                if 'dec' in target or 'tgl' in target:
                    lines[line_counter + x] = 'inc' + lines[line_counter + x][3:]
                elif 'inc' in target:
                    lines[line_counter + x] = 'dec' + lines[line_counter + x][3:]
                elif 'jnz' in target:
                    lines[line_counter + x] = 'cpy' + lines[line_counter + x][3:]
                else:
                    lines[line_counter + x] = 'jnz' + lines[line_counter + x][3:]
                print(lines[line_counter + x])
            line_counter += 1
        elif 'jnz' in l:
            m = re.search('jnz (\S+) (\d+)', l)
            if m is None:
                m = re.search('jnz (\S+) (-\d+)', l)
            if m is not None:
                r = m.group(1)
                if (r in 'abcd' and not(registers[r] == 0)):
                    line_counter += int(m.group(2))
                elif r.isnumeric() and not(int(r) == 0):
                    line_counter += int(m.group(2))
                else:
                    line_counter += 1
            else:
                m = re.search('jnz (\d+) (\w+)', l)
                if m is None:
                    m = re.search('jnz (-\d+) (\w+)', l)
                r = m.group(2)
                x = int(m.group(1))
                if (r in 'abcd' and not(x == 0)):
                    line_counter += registers[r]
                else:
                    line_counter += 1
        else:
            line_counter += 1

    print('Register a contains {}'.format(registers['a']))

if __name__ == "__main__":
    print('Part 1:')
    execute('day23_input.txt')
    print('Part 2:')
    execute('day23_input.txt', a_init=12)
