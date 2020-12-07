import re
import copy
CONTAINS_RE = re.compile('([0-9]+) (.*) bags?')


def parser(indata):
    rows = [entry for entry in indata.split('\n') if entry]
    bags = {}
    bag_counts = {}
    for row in rows:
        current = row[:row.index(' bags')]
        bags[current] = []
        for entry in row[row.index('contain ') + 8:].split(', '):
            if entry != 'no other bags.':
                bags[current].append((CONTAINS_RE.match(entry).groups()[1],
                                      int(CONTAINS_RE.match(entry).groups()[0])))
    return bags


def reverse_bags(bags):
    rev_bags = {}
    for bag in bags:
        if bag not in rev_bags:
            rev_bags[bag] = []
        for cont_bag in bags[bag]:
            if cont_bag[0] not in rev_bags:
                rev_bags[cont_bag[0]] = [bag]
            else:
                rev_bags[cont_bag[0]].append(bag)
    return rev_bags


def part1(rev_bags):
    new_bags = set()
    for new_target in rev_bags['shiny gold']:
        part1_recurse(rev_bags, new_target, new_bags)
    return len(new_bags)


def part1_recurse(rev_bags, target, new_bags):
    for new_target in rev_bags[target]:
        part1_recurse(rev_bags, new_target, new_bags)
    new_bags.add(target)


# answer will be one too great, since the first bag is included
def part2(bags, target = 'shiny gold'):
    count = 1
    for new_target in bags[target]:
        count += new_target[1]*part2(bags, new_target[0])
    return count


test_data1 = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

data = open('7.txt').read()

test_bags = parser(test_data1)
test_rev_bags = reverse_bags(test_bags)
print(part1(test_rev_bags))

test_data2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''
test_bags2 = parser(test_data2)
print(part2(test_bags2)-1)

bags = parser(data)
rev_bags = reverse_bags(bags)
print(part1(rev_bags))
print(part2(bags)-1)
