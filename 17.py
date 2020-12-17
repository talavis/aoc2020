import copy
import time
import itertools

def part1(data):
    def find_neighbours(x, y, z):
        return [(x+v[0], y+v[1], z+v[2]) for v in itertools.product((-1,0,1), repeat=3) if v != (0, 0, 0)]

    def step(coords):
        new_coords = set()
        for coord in coords:
            neighbours = find_neighbours(*coord)
            active = sum(1 for entry in neighbours if entry in coords)
            if 2 <= active <= 3:
                new_coords.add(coord)
            for entry in neighbours:
                if entry in coords:
                    continue
                neighs = find_neighbours(*entry)
                active = sum(1 for pos in neighs if pos in coords)
                if active == 3:
                    new_coords.add(entry)
        return new_coords

    # changes may only occur next to an existing '#'
    coords = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                coords.add((0, i, j))
    
    for i in range(6):
        coords = step(coords)

    return len(coords)


def part2(data):
    def find_neighbours(a, b, c, d):
        return [(a+v[0], b+v[1], c+v[2], d+v[3]) for v in itertools.product((-1,0,1), repeat=4) if v != (0, 0, 0, 0)]

    def step(coords):
        new_coords = set()
        for coord in coords:
            neighbours = find_neighbours(*coord)
            active = sum(1 for entry in neighbours if entry in coords)
            if 2 <= active <= 3:
                new_coords.add(coord)
            for entry in neighbours:
                if entry in coords:
                    continue
                neighs = find_neighbours(*entry)
                active = sum(1 for pos in neighs if pos in coords)
                if active == 3:
                    new_coords.add(entry)
        return new_coords

    # changes may only occur next to an existing '#'
    coords = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                coords.add((0, 0, i, j))
    
    for i in range(6):
        coords = step(coords)

    return len(coords)


test_data = [list(row) for row in '''.#.
..#
###'''.split('\n')]

print(f'Test for part 1 passed: {part1(test_data) == 112}')
print(f'Test for part 2 passed: {part2(test_data) == 848}')

data = [list(row) for row in '''..#..#..
#.#...#.
..#.....
##....##
#..#.###
.#..#...
###..#..
....#..#'''.split('\n')]

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
