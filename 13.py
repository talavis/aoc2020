import time

def part1(timestamp, buses):
    buses = [bus for bus in buses if bus != 'x']
    delays = [bus-timestamp % bus for bus in buses]

    first = min(delays)

    return first * buses[delays.index(first)]


def part2(buses):
    step = buses[0]
    ts = 0
    for i in range(1, len(buses)):
        if buses[i] == 'x':
            continue
        while (ts + i) % buses[i] != 0:
            ts += step
        step *= buses[i]
    return ts


test_data = (939, (7,13,'x','x',59,'x',31,19))

infile = open('13.txt')
ts = int(infile.readline().strip())
buses = list(int(bus) if bus != 'x' else 'x'for bus in infile.readline().strip().split(','))

print(part1(*test_data) == 295)

print(part2(test_data[1]) == 1068781)

times = []
for i in range(5):
    start = time.time()
    res = part1(ts, buses)
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')

times = []
for i in range(5):
    start = time.time()
    res = part2(buses)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')
