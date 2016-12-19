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

def steal_part2(nelves): # use 2 queues
    q1 = queue.Queue(maxsize=int(nelves/2)+1)
    q2 = queue.Queue(maxsize=int(nelves/2)+1)

    for i in range(int(nelves/2)):
        q1.put([i+1, 1]) # [elf id, n presents]
    for i in range(int(nelves/2), nelves):
        q2.put([i+1, 1]) # [elf id, n presents]

    elf = q1.get()
    q1_len = int(nelves/2)
    q2_len = nelves - int(nelves/2)

    while not q2.empty():
        to_steal = q2.get()
        elf[1] += to_steal[1]
        if q2.empty() and q1.empty():
            break
        if q2_len > q1_len:
            q1.put(q2.get())
            q2_len -= 1
        else:
            q1_len -= 1
        q2.put(elf)
        elf = q1.get()

    print('Elf {} has {} presents.'.format(elf[0], elf[1]))

if __name__ == "__main__":
    #steal_part1(3014387)
    steal_part2(3014387)
