import copy
import itertools

def part1(data):
    def step(data):
        new_data = copy.deepcopy(data)
        # first row:

        for entry in ((0, 0), (0, -1), (-1, 0), (-1, -1)):
            if data[entry[0]][entry[1]] != '.':
                new_data[entry[0]][entry[1]] = '#'

        for pos in range(1, len(data[0])-1):
            if data[0][pos] != '.':
                nearby = data[0][pos-1:pos+2] + data[1][pos-1:pos+2]
                if data[0][pos] == 'L' and not nearby.count('#'):
                    new_data[0][pos] = '#'
                elif data[0][pos] == '#':
                    if nearby.count('#') >= 5:  # since the seat itself is included
                        new_data[0][pos] = 'L'

        # last row
        for pos in range(1, len(data[0])-1):
            if data[-1][pos] != '.':
                nearby = data[-1][pos-1:pos+2] + data[-2][pos-1:pos+2]
                if data[-1][pos] == 'L' and not nearby.count('#'):
                    new_data[-1][pos] = '#'
                elif data[-1][pos] == '#':
                    if nearby.count('#') >= 5:  # since the seat itself is included
                        new_data[-1][pos] = 'L'
        # first col
        for row in range(1, len(data)-1):
            if data[row][0] != '.':
                nearby = data[row][1:2] + data[row-1][0:2] + data[row+1][0:2]
                if data[row][0] == 'L' and not nearby.count('#'):
                    new_data[row][0] = '#'
                elif data[row][0] == '#':
                    if nearby.count('#') >= 4:
                        new_data[row][0] = 'L'
        # last col
        for row in range(1, len(data)-1):
            if data[row][-1] != '.':
                nearby = (data[row][-2] +
                          data[row-1][-2] + data[row-1][-1] +
                          data[row+1][-2] + data[row+1][-1])
                if data[row][-1] == 'L' and not nearby.count('#'):
                    new_data[row][-1] = '#'
                elif data[row][-1] == '#':
                    if nearby.count('#') >= 4:
                        new_data[row][-1] = 'L'
        # all center fields
        for i in range(1,len(data)-1):
            for j in range(1, len(data[0])-1):
                if data[i][j] != '.':
                    nearby = list(itertools.chain.from_iterable(row[j-1:j+2] for row in data[i-1:i+2]))
                    if data[i][j] == 'L' and not nearby.count('#'):
                        new_data[i][j] = '#'
                    elif data[i][j] == '#':
                        if nearby.count('#') >= 5:  # since the seat itself is included
                            new_data[i][j] = 'L'
        return new_data
        
    def same(first, second):
        first = ''.join(''.join(row) for row in first)
        second = ''.join(''.join(row) for row in second)
        return first == second

    old_data = [['asd']]
    i = 0
    while not same(data, old_data):
        i += 1
        old_data = data
        data = step(data)
 
    taken_seats = 0
    for row in data:
        taken_seats += row.count('#')
    print('\n'.join([''.join(row) for row in data]))
    print()
    return taken_seats
    

def part2(data):
    def step(data):
        new_data = copy.deepcopy(data)
        # first row:

        for entry in ((0, 0), (0, -1), (-1, 0), (-1, -1)):
            if data[entry[0]][entry[1]] != '.':
                new_data[entry[0]][entry[1]] = '#'

        for pos in range(1, len(data[0])-1):
            if data[0][pos] != '.':
                nearby = data[0][pos-1:pos+2] + data[1][pos-1:pos+2]
                if data[0][pos] == 'L' and not nearby.count('#'):
                    new_data[0][pos] = '#'
                elif data[0][pos] == '#':
                    if nearby.count('#') >= 5:  # since the seat itself is included
                        new_data[0][pos] = 'L'

        # last row
        for pos in range(1, len(data[0])-1):
            if data[-1][pos] != '.':
                nearby = data[-1][pos-1:pos+2] + data[-2][pos-1:pos+2]
                if data[-1][pos] == 'L' and not nearby.count('#'):
                    new_data[-1][pos] = '#'
                elif data[-1][pos] == '#':
                    if nearby.count('#') >= 5:  # since the seat itself is included
                        new_data[-1][pos] = 'L'
        # first col
        for row in range(1, len(data)-1):
            if data[row][0] != '.':
                nearby = data[row][1:2] + data[row-1][0:2] + data[row+1][0:2]
                if data[row][0] == 'L' and not nearby.count('#'):
                    new_data[row][0] = '#'
                elif data[row][0] == '#':
                    if nearby.count('#') >= 4:
                        new_data[row][0] = 'L'
        # last col
        for row in range(1, len(data)-1):
            if data[row][-1] != '.':
                nearby = (data[row][-2] +
                          data[row-1][-2] + data[row-1][-1] +
                          data[row+1][-2] + data[row+1][-1])
                if data[row][-1] == 'L' and not nearby.count('#'):
                    new_data[row][-1] = '#'
                elif data[row][-1] == '#':
                    if nearby.count('#') >= 4:
                        new_data[row][-1] = 'L'
        # all center fields
        for i in range(1,len(data)-1):
            for j in range(1, len(data[0])-1):
                if data[i][j] != '.':
                    nearby = list(itertools.chain.from_iterable(row[j-1:j+2] for row in data[i-1:i+2]))
                    if data[i][j] == 'L' and not nearby.count('#'):
                        new_data[i][j] = '#'
                    elif data[i][j] == '#':
                        if nearby.count('#') >= 5:  # since the seat itself is included
                            new_data[i][j] = 'L'
        return new_data
        
    def same(first, second):
        first = ''.join(''.join(row) for row in first)
        second = ''.join(''.join(row) for row in second)
        return first == second

    old_data = [['asd']]
    i = 0
    while not same(data, old_data):
        i += 1
        old_data = data
        data = step(data)
 
    taken_seats = 0
    for row in data:
        taken_seats += row.count('#')
    print('\n'.join([''.join(row) for row in data]))
    print()
    return taken_seats


data = [list(val) for val in open('11.txt').read().split('\n') if val]

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

test_data2 = [list(row) for row in '''LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
L.LLLLLLLL
.LLLLLLLLL'''.split('\n')]

#print(part1(test_data))
#print(part1(test_data2))

#print(data)
print(part1(data))

