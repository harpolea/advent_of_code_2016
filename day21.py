import re

def scramble(in_file, in_str):

    def swap_pos(s, x, y):
        if x < y:
            return s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]
        else:
            return s[:y] + s[x] + s[y+1:x] + s[y] + s[x+1:]

    def swap_letter(s, x, y):
        i = s.index(x)
        j = s.index(y)
        if i < j:
            return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        else:
            return s[:j] + s[i] + s[j+1:i] + s[j] + s[i+1:]

    def rot_l(s, step):
        step = step % len(s)
        return s[step:] + s[:step]

    def rot_r(s, step):
        step = step % len(s)
        return s[-step:] + s[:-step]

    def rot_pos(s, l):
        step = s.index(l) + 1
        if step > 4:
            step += 1
        return rot_r(s, step)

    def reverse(s, x, y):
        if x < y:
            if (y + 1) < len(s):
                return s[:x] + s[x:y+1][::-1] + s[y+1:]
            else:
                return s[:x] + s[x:][::-1]
        else:
            if (x + 1) < len(s):
                return s[:y] + s[y:x+1][::-1] + s[x+1]
            else:
                return s[:y] + s[y:][::-1]

    def remove(s, x, y):
        if x < y:
            if y + 1 < len(s):
                return s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
            else:
                return s[:x] + s[x+1:] + s[x]
        else:
            if x + 1 < len(s):
                return s[:y] + s[x] + s[y:x] + s[x+1:]
            else:
                return s[:y] + s[x] + s[y:x]

    # read file
    f = open(in_file, 'r')

    for l in f:
        print(l,in_str)
        m = re.match('swap position (\d+) with position (\d+)', l)
        if m is not None:
            in_str = swap_pos(in_str, int(m.group(1)), int(m.group(2)))
        else:
            m = re.match('swap letter (\w+) with letter (\w+)', l)
            if m is not None:
                in_str = swap_letter(in_str, m.group(1), m.group(2))
            else:
                m = re.match('rotate left (\d+) step', l)
                if m is not None:
                    in_str = rot_l(in_str, int(m.group(1)))
                else:
                    m = re.match('rotate right (\d+) step', l)
                    if m is not None:
                        in_str = rot_r(in_str, int(m.group(1)))
                    else:
                        m = re.match('rotate based on position of letter (\w+)', l)
                        if m is not None:
                            in_str = rot_pos(in_str, m.group(1))
                        else:
                            m = re.match('reverse positions (\d+) through (\d+)', l)
                            if m is not None:
                                in_str = reverse(in_str, int(m.group(1)), int(m.group(2)))
                            else:
                                m = re.match('move position (\d+) to position (\d+)', l)
                                if m is not None:
                                    in_str = remove(in_str, int(m.group(1)), int(m.group(2)))

    print('Scrambled password is {}'.format(in_str))
    return

def unscramble(in_file, in_str):

    def swap_pos(s, x, y):
        if x < y:
            return s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]
        else:
            return s[:y] + s[x] + s[y+1:x] + s[y] + s[x+1:]

    def swap_letter(s, x, y):
        i = s.index(x)
        j = s.index(y)
        if i < j:
            return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        else:
            return s[:j] + s[i] + s[j+1:i] + s[j] + s[i+1:]

    def rot_l(s, step):
        step = step % len(s)
        return s[step:] + s[:step]

    def rot_r(s, step):
        step = step % len(s)
        return s[-step:] + s[:-step]

    def rot_pos(s, l):
        i = s.index(l)
        maps = [1, 3, 5, 7, 10, 12, 14, 16]
        m_dict = {}
        for j, m in enumerate(maps):
            m_dict[m % len(s)] = j
        step = (i - m_dict[i]) % len(s)
        return rot_l(s, step)

    def reverse(s, x, y):
        if x < y:
            if (y + 1) < len(s):
                return s[:x] + s[x:y+1][::-1] + s[y+1:]
            else:
                return s[:x] + s[x:][::-1]
        else:
            if (x + 1) < len(s):
                return s[:y] + s[y:x+1][::-1] + s[x+1]
            else:
                return s[:y] + s[y:][::-1]

    def remove(s, x, y):
        if x < y:
            if y + 1 < len(s):
                return s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
            else:
                return s[:x] + s[x+1:] + s[x]
        else:
            if x + 1 < len(s):
                return s[:y] + s[x] + s[y:x] + s[x+1:]
            else:
                return s[:y] + s[x] + s[y:x]

    # read file
    f = open(in_file, 'r')
    lines = f.readlines()

    for l in lines[::-1]:
        print(l,in_str)
        m = re.match('swap position (\d+) with position (\d+)', l)
        if m is not None:
            in_str = swap_pos(in_str, int(m.group(1)), int(m.group(2)))
        else:
            m = re.match('swap letter (\w+) with letter (\w+)', l)
            if m is not None:
                in_str = swap_letter(in_str, m.group(1), m.group(2))
            else:
                m = re.match('rotate left (\d+) step', l)
                if m is not None:
                    in_str = rot_r(in_str, int(m.group(1)))
                else:
                    m = re.match('rotate right (\d+) step', l)
                    if m is not None:
                        in_str = rot_l(in_str, int(m.group(1)))
                    else:
                        m = re.match('rotate based on position of letter (\w+)', l)
                        if m is not None:
                            in_str = rot_pos(in_str, m.group(1))
                        else:
                            m = re.match('reverse positions (\d+) through (\d+)', l)
                            if m is not None:
                                in_str = reverse(in_str, int(m.group(1)), int(m.group(2)))
                            else:
                                m = re.match('move position (\d+) to position (\d+)', l)
                                if m is not None:
                                    in_str = remove(in_str, int(m.group(2)), int(m.group(1)))

    print('Unscrambled password is {}'.format(in_str))
    return

if __name__ == "__main__":
    scramble('day21_input.txt', 'abcdefgh')
    unscramble('day21_input.txt', 'fbgdceah')
