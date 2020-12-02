#!/usr/bin/env python3

import itertools
import numpy

GOAL1 = 2020

def part1(data):
    a = 0
    b = len(data)-1
    
    while a < b:
        tmp = data[a] + data[b]
        if tmp == GOAL1:
            print(f'Part 1: {data[a]} * {data[b]} = {data[a] * data[b]}')
            return
        if tmp < GOAL1:
            a += 1
        else:
            b -= 1

def part2(data):
    for combo in itertools.combinations(data, 3):
        if sum(combo) == GOAL1:
            print(f'Part 2: {numpy.prod(combo)}')
            return


test_data1 = sorted([1721, 979, 366, 299, 675, 1456])

print('Testing:')
part1(test_data1)
print('Part 1: 299 * 1721 = 514579 (reference)')
part2(test_data1)
print('Part 2: 241861950 (reference)')

data1 = sorted([int(data) for data in open('1.txt').read().split('\n') if data])

print('Run:')
part1(data1)
part2(data1)
