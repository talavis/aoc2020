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

    def step(data):
        new_data = copy.deepcopy(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] != '.':
                    occupied = find_nearby(i, j)
                    if data[i][j] == 'L' and not occupied:
                        new_data[i][j] = '#'
                    elif data[i][j] == '#':
                        if occupied >= 4:
                            new_data[i][j] = 'L'
        return new_data

    neighbours = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbours[(i, j)] = find_neighbours(i, j)

    old_data = [['']]
    while not same(data, old_data):
        old_data = data
        data = step(data)

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
    
    def step(data):
        new_data = copy.deepcopy(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] != '.':
                    occupied = find_nearby(i, j)
                    if data[i][j] == 'L' and not occupied:
                        new_data[i][j] = '#'
                    elif data[i][j] == '#':
                        if occupied >= 5:
                            new_data[i][j] = 'L'
        return new_data
    
    neighbours = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbours[(i, j)] = find_neighbours(i, j)

    old_data = [['']]
    while not same(data, old_data):
        old_data = data
        data = step(data)
    taken_seats = 0
    for row in data:
        taken_seats += row.count('#')
    return taken_seats


data = [list(val) for val in open('11.txt').read().split('\n') if val]

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
