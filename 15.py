import time

class Pair:
    def __init__(self):
        self.values = [None]*2
    def add(self, new_value):
        self.values[0] = self.values[1]
        self.values[1] = new_value
    def __contains__(self, value):
        return self.values[1] is not None


def part1(indata, end=2020):
    spoken = {}
    for i, val in enumerate(indata[:-1]):
        spoken[val] = i
    latest = indata[-1]
    count = len(spoken)-1
    while count < end-2:
        count += 1
        if latest in spoken:
            orig = latest
            latest = count-spoken[latest]
            spoken[orig] = count
        else:
            spoken[latest] = count
            latest = 0
    return latest


data = [11, 18, 0, 20, 1, 7, 16]

test_data1 = [[0, 3, 6], [2, 3, 1], [3, 1, 2]]
test_answers1 = [436, 78, 1836]
test_answers2 = [175594, 6895259, 362]

for i, dat in enumerate(test_data1):
    print(part1(dat) == test_answers1[i])
#    print(part1(dat, end=30000000) == test_answers2[i])

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
    res = part1(data, end=30000000)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')
