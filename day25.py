import re
import io

def execute(input, a_init=0):
    registers = {'a':a_init, 'b':0, 'c':0, 'd':0}

    # read file
    f = io.StringIO(input)
    lines = f.readlines()
    
    signal = ""
    line_counter = 0

    while(line_counter < len(lines) and len(signal) < 100):
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
        elif 'out' in l:
            m = re.search('out (\S+)', l)
            r = m.group(1)
            if r in 'abcd':
                signal += str(registers[r])
            elif r.isnumeric():
                signal += str(r)
                
            if (len(signal) > 1 and ((int(signal[-1]) + int(signal[-2])) != 1 or (int(signal[-1]) * int(signal[-2])) != 0)):
                return False
            
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
    print(f'For a_init = {a_init}, signal is {signal}')
    return True

input = "cpy a d\ncpy 14 c\ncpy 182 b\ninc d\ndec b\njnz b -2\ndec c\njnz c -5\ncpy d a\njnz 0 0\ncpy a b\ncpy 0 a\ncpy 2 c\njnz b 2\njnz 1 6\ndec b\ndec c\njnz c -4\ninc a\njnz 1 -7\ncpy 2 b\njnz c 2\njnz 1 4\ndec b\ndec c\njnz 1 -4\njnz 0 0\nout b\njnz a -19\njnz 1 -21"

i = 0
while (not execute(input, i) and i < 1000):
    i += 1 
