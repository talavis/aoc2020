pp_data = [row for row in open('4.txt').read().split('\n')]

REQUIRED = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

test_data1 = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''.split('\n')


def part1(data):
    nr_valid = 0
    current = dict()
    for row in data:
        if row:
            entries = row.split(' ')
            for entry in entries:
                if entry:
                    vals = entry.split(':')
                    current[vals[0]] = vals[1]
        else:
            if REQUIRED.issubset(set(current.keys())):
                nr_valid += 1
            current = dict()
    return nr_valid

test_data2_inv = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''.split('\n')

test_data2_v = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''.split('\n')

import re
HCL = re.compile('^#[a-f0-9]{6}$')
PID = re.compile('^[0-9]{9}$')

def part2(data):
    nr_valid = 0
    current = dict()
    for row in data:
        if row:
            entries = row.split(' ')
            for entry in entries:
                if entry:
                    vals = entry.split(':')
                    current[vals[0]] = vals[1]
        else:
            if set(current.keys()) == REQUIRED or (REQUIRED.issubset(set(current.keys())) and (len(current.keys()) == len(REQUIRED)+1 and 'cid' in current.keys())):
                if 1920 <= int(current['byr']) <= 2002:
                    if 2010 <= int(current['iyr']) <= 2020:
                        if 2020 <= int(current['eyr']) <= 2030:
                            if (current['hgt'][-2:] == 'cm' and 150 <= int(current['hgt'][:-2]) <= 193) or\
                               (current['hgt'][-2:] == 'in' and 59 <= int(current['hgt'][:-2]) <= 76):
                                if HCL.match(current['hcl']):
                                    if current['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                        if PID.match(current['pid']):
                                            nr_valid += 1
            current = dict()
    return nr_valid


assert part1(test_data1) == 2

print(part1(pp_data))

#assert part2(test_data2_inv) == 0
#assert part2(test_data2_v) == 4

print(part2(pp_data))
