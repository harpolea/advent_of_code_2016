import re

def bots(in_file):
    # read file
    f = open(in_file, 'r')

    instructions = []
    bot_dict = {}
    output_dict = {}

    for line in f:
        line = line.replace('\n', '')
        instructions.append(line)

    def distribute():

        for i in instructions:
            m = re.search('value (\d+) goes to bot (\d+)', i)
            if m is not None:
                value = int(m.group(1))
                bot = int(m.group(2))
                if bot in bot_dict:
                    bot_dict[bot].add(value)
                else:
                    bot_dict[bot] = {value}
            #print(i)
            m = re.search('bot (\d+) gives low to bot (\d+) and high to bot (\d+)', i)
            n = re.search('bot (\d+) gives low to output (\d+) and high to bot (\d+)', i)
            p = re.search('bot (\d+) gives low to bot (\d+) and high to output (\d+)', i)
            q = re.search('bot (\d+) gives low to output (\d+) and high to output (\d+)', i)
            if m is not None:
                bot_donor = int(m.group(1))
                bot_low = int(m.group(2))
                bot_high = int(m.group(3))

                if bot_donor in bot_dict and len(bot_dict[bot_donor]) == 2:
                    if bot_low in bot_dict:
                        bot_dict[bot_low].add(min(bot_dict[bot_donor]))
                    else:
                        bot_dict[bot_low] = {min(bot_dict[bot_donor])}

                    if bot_high in bot_dict:
                        bot_dict[bot_high].add(max(bot_dict[bot_donor]))
                    else:
                        bot_dict[bot_high] = {max(bot_dict[bot_donor])}
            elif n is not None:
                bot_donor = int(n.group(1))
                output = int(n.group(2))
                bot_high = int(n.group(3))

                if bot_donor in bot_dict and len(bot_dict[bot_donor]) == 2:
                    if output in output_dict:
                        output_dict[output].add(min(bot_dict[bot_donor]))
                    else:
                        output_dict[output] = {min(bot_dict[bot_donor])}

                    if bot_high in bot_dict:
                        bot_dict[bot_high].add(max(bot_dict[bot_donor]))
                    else:
                        bot_dict[bot_high] = {max(bot_dict[bot_donor])}
            elif p is not None:
                bot_donor = int(p.group(1))
                bot_low = int(p.group(2))
                output = int(p.group(3))

                if bot_donor in bot_dict and len(bot_dict[bot_donor]) == 2:
                    if bot_low in bot_dict:
                        bot_dict[bot_low].add(min(bot_dict[bot_donor]))
                    else:
                        bot_dict[bot_low] = {min(bot_dict[bot_donor])}

                    if output in output_dict:
                        output_dict[output].add(max(bot_dict[bot_donor]))
                    else:
                        output_dict[output] = {max(bot_dict[bot_donor])}
            elif q is not None:
                bot_donor = int(q.group(1))
                output_low = int(q.group(2))
                output_high = int(q.group(3))

                if bot_donor in bot_dict and len(bot_dict[bot_donor]) == 2:
                    if output_low in output_dict:
                        output_dict[output_low].add(min(bot_dict[bot_donor]))
                    else:
                        output_dict[output_low] = {min(bot_dict[bot_donor])}

                    if output_high in output_dict:
                        output_dict[output_high].add(max(bot_dict[bot_donor]))
                    else:
                        output_dict[output_high] = {max(bot_dict[bot_donor])}


    for i in range(100): # need to loop for convergence
        distribute()

    print(bot_dict)
    print(output_dict)

    for key, s in bot_dict.items():
        if (61 in s and 17 in s):
            print('Bot comparing value-61 chips to value-17 chips is {}'.format(key))

    print('Product of chips in outputs 0, 1, 2 is {}'.format(output_dict[0].pop() * output_dict[1].pop() * output_dict[2].pop()))

if __name__ == "__main__":
    bots('day10_input.txt')
