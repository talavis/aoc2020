import collections

data_groups = open('6.txt').read().split('\n\n')

test_data = '''abc

a
b
c

ab
ac

a
a
a
a

b

'''.split('\n\n')

def part1(data):
    answersum = 0
    for group in data:
        answers = set(group)
        if '\n' in answers:
            answers.remove('\n')
        answersum += len(answers)
    return answersum


def part2(data):
    answersum = 0
    for group in data:
        nr_entries = group.count('\n')+1
        counts = collections.Counter(group)
        for entry in counts:
            if counts[entry] == nr_entries:
                answersum += 1
#                print(f'match ({entry}) in {counts} from {repr(group)}')
#            else:
#                print(f'no match for ({entry}) in {counts} from {repr(group)}')
    return answersum


print(part1(test_data))
print(part1(data_groups))

print(part2(test_data))
print(part2(data_groups))
