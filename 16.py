import tempfile
import time

def parser(infile):
    fields = []
    field_names = []
    while row := infile.readline().strip():
        field_names.append(row[:row.index(':')])
        cols = row[row.index(':'):].split(' ')
        fields.append(((int(cols[1][:cols[1].index('-')]),
                        int(cols[1][cols[1].index('-')+1:])),
                       (int(cols[3][:cols[3].index('-')]),
                        int(cols[3][cols[3].index('-')+1:]))))
    infile.readline()
    ticket = [int(num) for num in infile.readline().strip().split(',')]

    infile.readline()
    infile.readline()
    others = []
    while row := infile.readline().strip():
        others.append([int(num) for num in row.split(',')])

    return field_names, fields, ticket, others


def part1(fields, tickets):
    validity = [False]*1000
    for entry in fields:
        for ranges in entry:
            for i in range(ranges[0], ranges[1]+1):
                validity[i] = True

    invalid = []
    valids = []
    for ticket in tickets:
        valid = True
        for num in ticket:
            if not validity[num]:
                invalid.append(num)
                valid = False
        if valid:
            valids.append(ticket)

    return sum(invalid), valids


def part2(field_names, fields, ticket, others, test=False):
    others = others + [ticket]
    possible = [[] for _ in range(len(ticket))]
    for i in range(len(ticket)):
        values = [entry[i] for entry in others]
        for j, field in enumerate(fields):
            if all(field[0][0] <= val <= field[0][1] or
                   field[1][0] <= val <= field[1][1] for val in values):
                possible[j].append(i)

    field_pos = {field_name: None for field_name in field_names}
    while None in field_pos.values():
        for i, entry in enumerate(possible):
            if len(entry) == 1:
                val = entry[0]
                field_pos[field_names[i]] = val
                for field in possible:
                    if val in field:
                        field.remove(val)
    if test:
        return ticket[0]*ticket[1]*ticket[2]
    prod = 1
    for name in field_pos:
        if name.startswith('departure'):
            prod *= ticket[field_pos[name]]
    return prod

data = list(parser(open('16.txt')))

tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
''')

test_data1 = list(parser(open(tmpfile)))

test_res1 = part1(test_data1[1], test_data1[3])
print(f'Test for part 1 passed: {test_res1[0] == 71 and test_res1[1] == [[7, 3, 47]]}')

tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
''')
test_data2 = list(parser(open(tmpfile)))

test_res2 = part2(*test_data2, test=True)
print(f'Test for part 2 passed: {test_res2 == 12*11*13}')
print()

times = []
for i in range(5):
    start = time.time()
    res, valid = part1(data[1], data[3])
    stop = time.time()
    times.append((start, stop))
print(f'Part 1: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):e}s')
# remove invalid entries before part2
data[3] = valid

times = []
for i in range(5):
    start = time.time()
    res = part2(*data)
    stop = time.time()
    times.append((start, stop))
print(f'Part 2: {res}')
print(f'Average for {i+1} runs: {sum(e[1] - e[0] for e in times)/len(times):e}s')
