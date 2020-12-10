import functools

data = [0] + sorted(int(val) for val in open('10.txt').read().split('\n') if val)

def part1(data):
    current = 0
    jolt1 = 0
    jolt3 = 1

    for adapter in data:
        if adapter - current == 1:
            jolt1 += 1
        elif adapter - current == 3:
            jolt3 += 1
        current = adapter
    return(jolt1, jolt3)


def part2(data):
    @functools.cache
    def part2_rec(pos):
        if pos == len(data)-1:
            return 1
        combs = 0
        i = pos+1
        while i < len(data) and data[i] <= data[pos]+3:
            combs += part2_rec(i)
            i += 1
        return combs
    return part2_rec(0)


#test_data1 = sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4, 0])
#test_data2 = sorted([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3, 0])

#res = part1(test_data1)
#print(res[0]*res[1])

res = part1(data)
print(res[0]*res[1])

#print(part2(test_data1))
#print(part2(test_data2))
print(part2(data))
