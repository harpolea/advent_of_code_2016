import hashlib, re, collections

def find_index(salt, part_2=False):
    potential_keys = {}
    keys = []
    i = 0
    while len(keys) < 64:
        h = str(hashlib.md5(str.encode(salt + str(i))).hexdigest())
        if part_2:
            for i in range(2016):
                h = hashlib.md5(str.encode(h)).hexdigest()
        # test potential_keys to see if found multiple of five
        to_remove = set()
        for key, value in potential_keys.items():
            if (i - key) > 1000:
                to_remove.add(key)
            else:
                regex = r"(" + re.escape(str(value)) + r")\1\1\1\1"
                m = re.search(regex, h)
                if m is not None:
                    keys.append(key)
                    to_remove.add(key)
        for k in to_remove:
            potential_keys.pop(k)

        m = re.search(r'(\w)\1\1', h)
        if m is not None: # found potential key
            potential_keys[i] = m.group()[0]
        i+= 1

    print(sorted(keys))
    print("Index of 64th key is: {}".format(sorted(keys)[63]))

if __name__ == "__main__":
    salt = "zpqevtbw"
    find_index(salt)
    print('Part 2:')
    find_index(salt, part_2=True)
