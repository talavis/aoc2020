import copy
import sys

data = [row.split() for row in open('8.txt').read().split('\n') if row]
data = [[row[0], int(row[1]), False] for row in data]

# part 1

i = 0
acc = 0

used = [False]*len(data)
        
while not used[i]:
    used[i] = True
    if data[i][0] == 'acc':
        acc += data[i][1]
        i += 1
    elif data[i][0] == 'jmp':
        i += data[i][1]
    else:
        i += 1

print(acc)

# part 2
def test_change(i, acc, data, used):
    used = used[:]
    while i < len(data) and not used[i]:
        used[i] = True
        if data[i][0] == 'acc':
            acc += data[i][1]
            i += 1
        elif data[i][0] == 'jmp':
            i += data[i][1]
        else:
            i += 1
    if i == len(data):
        return True, acc
    return False, -1


i = 0
acc = 0
used = [False]*len(data)

while i < len(data):
    used[i] = True
    if data[i][0] == 'acc':
        acc += data[i][1]
        i += 1
        continue
    elif data[i][0] == 'jmp':
        res = test_change(i+1, acc, data, used)
        if res[0]:
            print(res[1])
            sys.exit(0)
        i += data[i][1]
    else:
        res = test_change(i+data[i][1], acc, data, used)
        if res[0]:
            print(res[1])
            sys.exit(0)
        i += 1

