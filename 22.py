import tempfile
import time

def parser(infile):
    decks = [[], []]
    nr = 0
    for row in infile:
        if row.startswith('Player'):
            continue
        if not row.strip():
            nr += 1
            continue
        decks[nr].append(int(row.strip()))
    return decks


def part1(decks):
    decks = [list(decks[0]), list(decks[1])]
    while decks[0] and decks[1]:
        card0 = decks[0].pop(0)
        card1 = decks[1].pop(0)
        if card0 > card1:
            decks[0].extend([card0, card1])
        else:
            decks[1].extend([card1, card0])

    if decks[0]:
        cards = decks[0]
    else:
        cards = decks[1]
    i = len(cards)
    total = 0
    for card in cards:
        total += i*card
        i -= 1
    return total


def part2(decks):
    def rec(deck0, deck1):
        used = set()
        deck0 = list(deck0)
        deck1 = list(deck1)
        while deck0 and deck1:
            if tuple(deck0) in used:
                return True, deck0
            used.add(tuple(deck0))
            card0 = deck0.pop(0)
            card1 = deck1.pop(0)
            if len(deck0) >= card0 and len(deck1) >= card1:
                zero_won, _ = rec(deck0[:card0], deck1[:card1])
            else:
                zero_won = card0 > card1
            if zero_won:
                deck0.extend([card0, card1])
            else:
                deck1.extend([card1, card0])
        return bool(deck0), deck0 if deck0 else deck1

    _, cards = rec(decks[0], decks[1])
    i = len(cards)
    total = 0
    for card in cards:
        total += i*card
        i -= 1
    return total


tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10''')
test_data = parser(open(tmpfile))
print(f'Test for part 1 passed: {part1(test_data) == 306}')
print(f'Test for part 2 passed: {part2(test_data) == 291}')

data = parser(open('22.txt'))

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
