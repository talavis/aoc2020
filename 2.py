data = [row.split(' ') for row in open('2.txt').read().split('\n') if row]

nr_valid1 = 0
nr_valid2 = 0

for entry in data:
    limit = [int(val) for val in entry[0].split('-')]
    char = entry[1][0]
    passwd = entry[2]
    if passwd.count(char) >= limit[0] and passwd.count(char) <= limit[1]:
        nr_valid1 += 1
    if (passwd[limit[0]-1] == char) != (passwd[limit[1]-1] == char):
        nr_valid2 += 1

print(nr_valid1)

print(nr_valid2)

