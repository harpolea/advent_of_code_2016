from copy import deepcopy

def safe(in_str, nrows):
    # translate into bools
    row = [True] * (len(in_str) + 2)
    for i in range(len(in_str)):
        if in_str[i] == '^':
            row[i+1] = False
    nsafe = sum(row[1:-1])

    counter = 1
    while counter < nrows:
        new_row = deepcopy(row)
        for i in range(1,len(in_str)+1):
            if ((not row[i-1]) and (not row[i]) and row[i+1]) or (row[i-1] and (not row[i]) and (not row[i+1])) or (row[i] and row[i+1] and (not row[i-1])) or (row[i-1] and row[i] and (not row[i+1])):
                new_row[i] = False
            else:
                new_row[i] = True
        row = new_row
        nsafe += sum(row[1:-1])
        counter += 1

    print('There are {} safe tiles'.format(nsafe))

if __name__ == "__main__":
    in_str = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"
    safe(in_str, 400000)
