import tempfile
import time

def simulate(current, cups_map, steps):
    highest = max(cups_map)
    for _ in range(steps):
        ext1 = cups_map[current]
        ext2 = cups_map[ext1]
        ext3 = cups_map[ext2]
        target = current-1 or highest
        while target == ext1 or target==ext2 or target == ext3:
            target = target-1 or highest
        cups_map[current] = cups_map[ext3]
        cups_map[ext3] = cups_map[target]
        cups_map[target] = ext1
        current = cups_map[current]
    return cups_map


def part1(data):
    cups_map = {}
    cups_map[data[-1]] = data[0]
    for i in range(0, len(data)-1):
        cups_map[data[i]] = data[i+1]

    new_map = simulate(data[0], cups_map, 100)

    current = new_map[1]
    vals = []
    while current != 1:
        vals.append(current)
        current = new_map[current]
    return ''.join([str(val) for val in vals])


def part2(data):
    cups_map = {}
    # cyclic
    cups_map[1_000_000] = data[0]
    # defined
    for i in range(0, len(data)-1):
        cups_map[data[i]] = data[i+1]
    cups_map[data[-1]] = max(data)+1
    # rest
    for i in range(max(data)+1, 1_000_000):
        cups_map[i] = i+1

    new_map = simulate(data[0], cups_map, 10_000_000)

    val1 = new_map[1]
    val2 = new_map[val1]
    return val1*val2


test_data = [int(nr) for nr in '389125467']
print(f'Test for part 1 passed (100): {part1(test_data) == "67384529"}')
print(f'Test for part 2 passed: {part2(test_data) == 149245887792}')

data = [int(nr) for nr in '193467258']

times = []
for i in range(5):
    start = time.time()
    res = part1(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):e}s')

times = []
for i in range(5):
    start = time.time()
    res = part2(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):e}s')
