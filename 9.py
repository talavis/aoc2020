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

i = 0
j = i
valsum = 0
while valsum != data[pos]:
    while valsum < data[pos]:
        valsum += data[j]
        j += 1
    while valsum > data[pos]:
        valsum -= data[i]
        i += 1

print(max(data[i:j])+min(data[i:j]))
