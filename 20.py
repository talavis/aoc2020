import copy
import re
import time

def parser(infile):
    tiles = {}
    tile = []
    nr = -1
    for row in infile:
        if row.startswith('Tile'):
            nr = int(row[5:-2])
        elif not row.strip():
            tiles[nr] = tile
            tile = []
            nr = -1
        else:
            tile.append(row.strip())
    if nr != -1:
        tiles[nr] = tile
    return tiles


def build_image(tiles):
    per_row = int(len(tiles)**0.5)
    unit_size = len(tiles[0])-2
    side_len = per_row*unit_size
    matrix = [['.']*side_len for _ in range(side_len)]
    for i, tile in enumerate(tiles):
        col = i % per_row * unit_size
        row = i // per_row * unit_size
        for r in range(unit_size):
            for c in range(unit_size):
                if tile[r+1][c+1] == '#':
                    matrix[row+r][col+c] = '#'
    matrix = [''.join(row) for row in matrix]
    return matrix


def part1(tiles):
    def rotate(tile):
        return [''.join(ele) for ele in zip(*tile[::-1])]
    def flip(tile):
        return tile[::-1]
    def left(tile):
        return ''.join([row[0] for row in tile])
    def top(tile):
        return ''.join(tile[0])
    def bottom(tile):
        return ''.join(tile[-1])
    def right(tile):
        return ''.join([row[-1] for row in tile])

    def rec(added, pos):
#        print(' '*pos, added)
#        if existing:
#            print('\n'.join([' '*pos + ''.join(row) for row in existing[-1]]))
        if len(added) == len(choices):
            return True

        for i in range(len(choices)):
            if choices[i] in added:
                continue
            added.append(choices[i])
            if pos < side_len:  # first row
                if pos == 0:  # first column
                    tile = tiles[choices[i]]
                    for f in range(2):
                        for r in range(4):
                            existing.append(tile)
                            if rec(added, pos+1):
                                return True
                            existing.pop()
                            tile = rotate(tile)
                        tile = flip(tile)

                else:  # other columns
                    tile = tiles[choices[i]]
                    for f in range(2):
                        for r in range(4):
                            if left(tile) == right(existing[-1]):
                                existing.append(tile)
                                if rec(added, pos+1):
                                    return True
                                existing.pop()
                            tile = rotate(tile)
                        tile = flip(tile)

            else:
                if pos % side_len == 0:  # first column
                    tile = tiles[choices[i]]
                    for f in range(2):
                        for r in range(4):
                            if top(tile) == bottom(existing[pos-side_len]):
                                existing.append(tile)
                                if rec(added, pos+1):
                                    return True
                                existing.pop()
                            tile = rotate(tile)
                        tile = flip(tile)

                else:  # other columns
                    tile = tiles[choices[i]]
                    for f in range(2):
                        for r in range(4):
                            if (top(tile) == bottom(existing[pos-side_len]) and
                                left(tile) == right(existing[-1])):
                                existing.append(tile)
                                if rec(added, pos+1):
                                    return True
                                existing.pop()
                            tile = rotate(tile)
                        tile = flip(tile)
            added.pop()
        return False

    side_len = int(len(tiles)**0.5)
    choices = list(tiles.keys())
    existing = []
    added = []
    rotations = []
    rec(added, 0)
    return added[0] * added[side_len-1] * added[len(added)-side_len] * added[len(added)-1], added, existing

"""
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
def part2(matrix):
    def rotate(tile):
        return [''.join(ele) for ele in zip(*tile[::-1])]
    def flip(tile):
        return tile[::-1]

    row_len = len(matrix[0])
    m_regex_text = ('#' + '.'*(row_len-19) +
                    '#....##....##....###' +'.'*(row_len-19) +
                    '#..#..#..#..#..#')
    monster_parts = m_regex_text.count('#')
    monster_pos = [i for i, ch in enumerate(m_regex_text) if ch == '#']
    monster_finder = re.compile(m_regex_text)
    for f in range(2):
        for r in range(4):
            as_str = ''.join(matrix)
            used = [False] * len(as_str)
            index = 0
            while hit := monster_finder.search(as_str[index:]):
                for i in range(len(monster_pos)):
                    used[hit.span()[0] + index + monster_pos[i]] = True
                index += hit.span()[0]+1
            if sum(used) > 0:
                return as_str.count('#') - sum(used)
            matrix = rotate(matrix)
        matrix = flip(matrix)


test_data = parser(open('20_test.txt'))
test_res = part1(test_data)
print(f'Test for part 1 passed: {test_res[0] == 20899048083289}')
test_matrix = build_image(test_res[2])
print(f'Test for part 2 passed: {part2(test_matrix) == 273}')

data = parser(open('20.txt'))
res = part1(data)
print(res[0])
data_matrix = build_image(res[2])
print(part2(data_matrix))

import sys
sys.exit(1)

times = []
for i in range(5):
    start = time.time()
    res = part1(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res[0]}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):e}s')

times = []
for i in range(5):
    start = time.time()
    res = part2(data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):e}s')
