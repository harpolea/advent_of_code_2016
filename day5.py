import hashlib

def find_code_part_1(in_str):
    pwd = ''
    i = 0
    while len(pwd) < 8:
        m = hashlib.md5(str.encode(in_str + str(i))).hexdigest()
        if m[:5] == '00000':
            print(m[5])
            pwd += m[5]
        i += 1

    print("Password is: {}".format(pwd))

def find_code_part_2(in_str):
    pwd = [None] * 8
    total_found = 0
    i = 0
    while total_found < 8:
        m = hashlib.md5(str.encode(in_str + str(i))).hexdigest()
        if m[:5] == '00000':
            if m[5].isnumeric() and int(m[5]) <= 7 and (pwd[int(m[5])] is None):
                pwd[int(m[5])] = m[6]
                print(m[6])
                total_found += 1
        i += 1

    print("Password is: {}".format(''.join(pwd)))

if __name__ == "__main__":
    in_str = "ugkcyxxp"
    #in_str = "abc"
    #find_code_part_1(in_str)
    find_code_part_2(in_str)
