import tempfile
import time

def parser(infile):
    directions = ('nw', 'ne', 'e', 'w', 'sw', 'se')
    rows = [row for row in infile.read().split('\n') if row]
    data = []
    for row in rows:
        data.append([])
        i = 0
        while i < len(row):
            for direction in directions:
                if row[i:].startswith(direction):
                    data[-1].append(direction)
                    i += len(direction)
    return data


def part1(data):
    coords = []
    for row in data:
        coord = [0, 0]
        for d in row:
            if d == 'nw':
                coord[0] -= 1
                coord[1] += 2
            elif d == 'ne':
                coord[0] += 1
                coord[1] += 2
            elif d == 'sw':
                coord[0] -= 1
                coord[1] -= 2
            elif d == 'se':
                coord[0] += 1
                coord[1] -= 2
            elif d == 'e':
                coord[0] += 2
            elif d == 'w':
                coord[0] -= 2
            else:
                print('bug')
        if coord in coords:
            coords.remove(coord)
        else:
            coords.append(coord)
    return len(coords), coords

DIRECTIONS = ((-1, 2), (1, 2), (-1, -2), (1, -2), (2, 0), (-2, 0))

def part2(black_tiles):
    def find_neighbours(tile):
        return [(tile[0]+d[0], tile[1]+d[1]) for d in DIRECTIONS]
    def find_black(tile, black_tiles):
        black = 0
        for d in DIRECTIONS:
            if (tile[0]+d[0], tile[1]+d[1]) in black_tiles:
                black += 1
        return black

    black_tiles = set(tuple(tile) for tile in black_tiles)
    for _ in range(100):
        to_check = list()
        for tile in black_tiles:
            to_check += find_neighbours(tile)
        to_check = set(to_check)

        new_black = set()
        for tile in to_check:
            nr_black = find_black(tile, black_tiles)
            if tile in black_tiles:
                if nr_black in (1, 2):
                    new_black.add(tile)
            else:
                if nr_black == 2:
                    new_black.add(tile)
        black_tiles = new_black
    return len(new_black)


tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
''')
test_data = parser(open(tmpfile))

res, test_black_tiles = part1(test_data)
print(f'Test for part 1 passed: {res == 10}')
print(f'Test for part 2 passed: {part2(test_black_tiles) == 149245887792}')

data = parser(open('24.txt'))

times = []
for i in range(5):
    start = time.time()
    res = part1(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res[0]}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):.2e}s')

black_tiles = res[1]

times = []
for i in range(5):
    start = time.time()
    res = part2(black_tiles)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):.2e}s')
