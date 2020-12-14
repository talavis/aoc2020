import math
import time

def part1(data):
    memory = {}
    mask = []
    for row in data:
        if row[0].startswith('mem'):
            addr = int(row[0][4:-1])
            val = bin(int(row[2]))[2:].rjust(36, '0')
            for op in mask:
                val = val[:op[0]] + op[1] + val[op[0]+1:]
            memory[addr] = int(val, 2)
        else:
            mask = tuple((i, val) for i, val in enumerate(row[2]) if val != 'X')
    return sum(memory.values())


def part2(data):
    memory = {}
    mask = []
    for row in data:
        if row[0].startswith('mem'):
            addr = bin(int(row[0][4:-1]))[2:].rjust(36, '0')
            val = int(row[2])
            for op in mask:
                addr = addr[:op[0]] + op[1] + addr[op[0]+1:]
            addrs = [addr]
            while True:
                try:
                    addrs_new = []
                    for addr in addrs:
                        i = addr.index('X')
                        addrs_new.append(addr[:i] + '0' + addr[i+1:])
                        addrs_new.append(addr[:i] + '1' + addr[i+1:])
                    addrs = addrs_new
                except ValueError:
                    break

            for addr in addrs:
                memory[addr] = val
        else:
            mask = sorted(((i, val) for i, val in enumerate(row[2]) if val != '0'), key = lambda x: x[1])
    return sum(memory.values())


data = [val.split(' ') for val in open('14.txt').read().split('\n') if val]

test_data1 = [val.split(' ') for val in '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.split('\n')]

test_data2 = [val.split(' ') for val in '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split('\n')]


#print(part1(test_data1) == 165)
#print(part2(test_data2) == 208)

times = []
for i in range(5):
    start = time.time()
    res = part1(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')

times = []
for i in range(5):
    start = time.time()
    res = part2(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')
