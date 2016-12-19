import queue

def steal_part1(nelves):
    q = queue.Queue(maxsize=nelves)
    for i in range(nelves):
        q.put([i+1, 1]) # [elf id, n presents]

    elf = q.get()

    while not q.empty():
        to_steal = q.get()
        elf[1] += to_steal[1]
        q.put(elf)
        elf = q.get()

    print('Elf {} has {} presents.'.format(elf[0], elf[1]))

if __name__ == "__main__":
    steal_part1(3014387)
