import tempfile
import re

def parser(infile):
    rules = {}
    start = []
    for row in infile:
        cols = row.split()
        if not cols:
            break
        rules[cols[0][:-1]] = ' '.join([col.strip('"') for col in cols[1:]])
    data = [row.strip() for row in infile]
    return rules, data


def part1(rules, data):
    rules = dict(rules)
    re_digit = re.compile('[0-9]')
    while re_digit.search(rules['0']):
        rule_keys = tuple(rules.keys())
        for key in rule_keys:
            if key == '0':
                continue
            if not re_digit.search(rules[key]):
                value = rules[key]
                del rules[key]
                for rule in rules:
                    rules[rule] = rules[rule].replace(f' {key} ', f' ({value}) ')
                    if rules[rule] == key:
                        rules[rule] = f'({value})'
                    if rules[rule].startswith(key + ' '):
                        rules[rule] = f'({value})' + rules[rule][len(key):]
                    if rules[rule].endswith(' ' + key):
                        rules[rule] = rules[rule][:-len(key)] + f'({value})'

    regex = re.compile(f'^{rules["0"].replace(" ","")}$')
    count = 0
    for dat in data:
        if regex.match(dat):
            count += 1
    return count


def part2(rules, data):
    saved = {}
    rules = dict(rules)
    re_digit = re.compile('[0-9]')
    while re_digit.search(rules['0']) :
        rule_keys = tuple(rules.keys())
        for key in rule_keys:
            if key == '0':
                continue
            if not re_digit.search(rules[key]):
                value = rules[key]
                if key in ('8', '11', '31', '42'):
                    if key == '8':
                        value = f'{value}+'
                    if key == '11':
                        value = f'({saved["42"]})+ ({saved["31"]})+'
                    saved[key] = value
                del rules[key]
                for rule in rules:
                    rules[rule] = rules[rule].replace(f' {key} ', f' ({value}) ')
                    if rules[rule] == key:
                        rules[rule] = f'({value})'
                    if rules[rule].startswith(key + ' '):
                        rules[rule] = f'({value})' + rules[rule][len(key):]
                    if rules[rule].endswith(' ' + key):
                        rules[rule] = rules[rule][:-len(key)] + f'({value})'


    regex = re.compile(f'^{rules["0"].replace(" ","")}$')
    regex2_text = f'^({saved["8"].replace(" ","")})+({saved["42"].replace(" ","")}){{asd}}({saved["31"].replace(" ","")}){{asd}}$'
    count = 0
    for dat in data:
        if regex.match(dat):
            for i in range(10):
                match = re.match(regex2_text.replace('asd', str(i)), dat)
                if match:
                    count += 1
                    break
    return count


tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
''')
test_data1 = parser(open(tmpfile))

tmpfile = tempfile.mkstemp()[1]
open(tmpfile, 'w').write('''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
''')
test_data2 = parser(open(tmpfile))

if (res := part1(*test_data1)) != 2:
    print(res, 'Fail')
if (res := part1(*test_data2)) != 3:
    print(res, 'Fail')
if (res := part2(*test_data2)) != 12:
    print(res, 'Fail')

data = parser(open('19.txt'))

print(f'Part 1: {part1(*data)}')

print(f'Part 2: {part2(*data)}')
