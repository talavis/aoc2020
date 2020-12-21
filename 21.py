import itertools
import re
import tempfile
import time

def parser(infile):
    combos = {}
    parse = re.compile('(.+) \(contains(.*)\)')
    for row in infile:
        if not row.strip():
            continue
        parts = parse.match(row).groups()
        combos[tuple(parts[0].split())] = [part.strip().strip(',') for part in parts[1].split()]
    return combos


def part1(food_list):
    allergens = set(itertools.chain.from_iterable(food_list.values()))
    foods = set(itertools.chain.from_iterable(food_list.keys()))
    base_dict = {allergen: 0 for allergen in allergens}
    base_dict['count'] = 0

    obs_food = {}
    obs_alg = {alg: {'count': 0} for alg in allergens}
    for combo in food_list.keys():
        algs = food_list[combo]
        for alg in algs:
            obs_alg[alg]['count'] += 1
        for food in combo:
            if food not in obs_food:
                obs_food[food] = dict(base_dict)
            for alg in algs:
                obs_food[food][alg] += 1
            obs_food[food]['count'] += 1

            for alg in algs:
                if food in obs_alg[alg]:
                    obs_alg[alg][food] += 1
                else:
                    obs_alg[alg][food] = 1
    for alg in obs_alg:
        for food in obs_alg[alg]:
            if food == 'count':
                continue
            if obs_alg[alg][food] == obs_alg[alg]['count']:
                if food in foods:
                    foods.remove(food)
    total = 0
    for food in foods:
        total += obs_food[food]['count']
    return total


def part2(food_list):
    allergens = set(itertools.chain.from_iterable(food_list.values()))
    foods = set(itertools.chain.from_iterable(food_list.keys()))
    base_dict = {allergen: 0 for allergen in allergens}
    base_dict['count'] = 0

    obs_food = {}
    obs_alg = {alg: {'count': 0} for alg in allergens}
    for combo in food_list.keys():
        algs = food_list[combo]
        for alg in algs:
            obs_alg[alg]['count'] += 1
        for food in combo:
            if food not in obs_food:
                obs_food[food] = dict(base_dict)
            for alg in algs:
                obs_food[food][alg] += 1
            obs_food[food]['count'] += 1

            for alg in algs:
                if food in obs_alg[alg]:
                    obs_alg[alg][food] += 1
                else:
                    obs_alg[alg][food] = 1

    may = {alg: set() for alg in allergens}
    for alg in obs_alg:
        for food in obs_alg[alg]:
            if food == 'count':
                continue
            if obs_alg[alg][food] == obs_alg[alg]['count']:
                may[alg].add(food)
    chosen = []
    ch_allergens = []
    while len(may) > 0:
        for entry in may:
            if len(may[entry]) == 1:
                chosen.append(may[entry].pop())
                ch_allergens.append(entry)
                for oentry in may:
                    if chosen[-1] in may[oentry]:
                        may[oentry].remove(chosen[-1])
                del may[entry]
                break
    sorted_chalg = sorted(ch_allergens)
    order = [ch_allergens.index(entry) for entry in sorted_chalg]
    return ','.join([chosen[i] for i in order])


tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)''')
test_data = parser(open(tmpfile))
print(f'Test for part 1 passed: {part1(test_data) == 5}')
print(f'Test for part 2 passed: {part2(test_data) == "mxmxvkd,sqjhc,fvjkl"}')

data = parser(open('21.txt'))

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
