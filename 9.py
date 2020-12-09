data = [int(val) for val in open('9.txt').read().split('\n') if val]

def is_sum(pos, data):
    for i in range(pos-25, pos):
        for j in range(i+1, pos):
            if data[i]+data[j] == data[pos]:
                return True

pos = 25
while is_sum(pos, data):
    pos += 1
print(data[pos])

for i in range(pos):
    j = i
    valsum = 0
    minnum=data[j]
    maxnum=data[j]
    while valsum < data[pos]:
        valsum += data[j]
        if data[j] > maxnum:
            maxnum = data[j]
        elif data[j] < minnum:
            minnum = data[j]
        j += 1
    if valsum == data[pos]:
        print(maxnum+minnum)
        break


