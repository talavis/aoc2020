import copy
import time
import itertools

        
def same(first, second):
    first = ''.join(''.join(row) for row in first)
    second = ''.join(''.join(row) for row in second)
    return first == second


def part1(data):
    def find_neighbours(r, c):
        nearby = []
        for direction in ((1,1), (1, -1), (-1, 1), (-1, -1),
                          (1, 0), (-1, 0), (0, 1), (0, -1)):
            i = r + direction[0]
            j = c + direction[1]
            if (0 <= i < len(data) and
                0 <= j < len(data[0])):
                nearby.append((i, j))
        return nearby

    def find_nearby(r, c):
        return [data[entry[0]][entry[1]] for entry in neighbours[(r, c)]].count('#')

    def step(data, new_data):
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] != '.':
                    occupied = find_nearby(i, j)
                    if data[i][j] == 'L':
                        if not occupied:
                            new_data[i][j] = '#'
                        else:
                            new_data[i][j] = 'L'
                    elif data[i][j] == '#':
                        if occupied >= 4:
                            new_data[i][j] = 'L'
                        else:
                            new_data[i][j] = '#'

    neighbours = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbours[(i, j)] = find_neighbours(i, j)

    data2 = copy.deepcopy(data)
    step(data, data2)
    while not same(data, data2):
        step(data, data2)
        data2, data = data, data2

    taken_seats = 0
    for row in data:
        taken_seats += row.count('#')
    return taken_seats


def part2(data):
    def find_neighbours(r, c):
        nearby = []
        for direction in ((1,1), (1, -1), (-1, 1), (-1, -1),
                          (1, 0), (-1, 0), (0, 1), (0, -1)):
            if (0 <= r + direction[0] < len(data) and
                0 <= c + direction[1] < len(data[0])):
                i = r + direction[0]
                j = c + direction[1]
            else:
                continue

            while (0 <= i + direction[0] < len(data) and
                   0 <= j + direction[1] < len(data[0]) and
                   data[i][j] == '.'):
                i += direction[0]
                j += direction[1]
            if not (i == r and j == c):
                nearby.append((i, j))
        return nearby

    def find_nearby(r, c):
        return [data[entry[0]][entry[1]] for entry in neighbours[(r, c)]].count('#')
    
    def step(data, new_data):
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] != '.':
                    occupied = find_nearby(i, j)
                    if data[i][j] == 'L':
                        if not occupied:
                            new_data[i][j] = '#'
                        else:
                            new_data[i][j] = 'L'
                    elif data[i][j] == '#':
                        if occupied >= 5:
                            new_data[i][j] = 'L'
                        else:
                            new_data[i][j] = '#'
    
    neighbours = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbours[(i, j)] = find_neighbours(i, j)

    data2 = copy.deepcopy(data)
    step(data, data2)
    while not same(data, data2):
        step(data, data2)
        data2, data = data, data2

    taken_seats = 0
    for row in data:
        taken_seats += row.count('#')
    return taken_seats


test_data = [list(row) for row in '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split('\n')]

#print(part1(test_data))

data = [list(val) for val in open('11.txt').read().split('\n') if val]

times = []
for i in range(5):
    start = time.time()
    res = part1(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')

data = [list(val) for val in open('11.txt').read().split('\n') if val]

times = []
for i in range(5):
    start = time.time()
    res = part2(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times)}')
