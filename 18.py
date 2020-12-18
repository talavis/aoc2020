def part1(data):
    def recur(ds):
        if not ds:
            return 0

        para_i = -1
        para_ds = []
        para_res = []
        for para in range(ds.count('(')):
            para_i = ds.index('(', para_i+1)
            pi = para_i+1
            pn = 0
            while ds[pi] != ')' or pn > 0:
                if ds[pi] == '(':
                    pn += 1
                elif ds[pi] == ')':
                    pn -= 1
                pi += 1
            para_ds.append(ds[para_i+1:pi])
            para_res.append(recur(para_ds[-1]))
        for entry, res in zip(para_ds, para_res):
            ds = ds.replace('(' + entry + ')', str(res))
        data = ds.split(' ')

        result = int(data[0])
        for i in range(2, len(data), 2):
            if data[i-1] == '+':
                result += int(data[i])
            else:
                result *= int(data[i])
        return result

    res = 0
    for entry in data:
        res += recur(entry)
    return res


def part2(data):
    def recur(ds):
        if not ds:
            return 0

        para_i = -1
        para_ds = []
        para_res = []
        for para in range(ds.count('(')):
            para_i = ds.index('(', para_i+1)
            pi = para_i+1
            pn = 0
            while ds[pi] != ')' or pn > 0:
                if ds[pi] == '(':
                    pn += 1
                elif ds[pi] == ')':
                    pn -= 1
                pi += 1
            para_ds.append(ds[para_i+1:pi])
            para_res.append(recur(para_ds[-1]))
        for entry, res in zip(para_ds, para_res):
            ds = ds.replace('(' + entry + ')', str(res))

        data = ds.split(' ')
        i = 0
        while i < len(data):
            if data[i] == '+':
                data = data[:i-1] + [str(int(data[i-1]) + int(data[i+1]))] + data[i+2:]
            else:
                i += 1

        result = 1
        for i in range(0, len(data), 2):
            result *= int(data[i])
        return result

    res = 0
    for entry in data:
        res += recur(entry)
    return res



data = open('18.txt').read().split('\n')

test_data1 = [('1 + 2 * 3 + 4 * 5 + 6', 71),
              ('2 * 3 + (4 * 5)', 26),
              ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)]

for entry in test_data1:
    if (res := part1([entry[0]])) != entry[1]:
        print(res, entry[1], 'Fail')

test_data2 = [('1 + 2 * 3 + 4 * 5 + 6', 231),
              ('2 * 3 + (4 * 5)', 46),
              ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340)]

for entry in test_data2:
    if (res := part2([entry[0]])) != entry[1]:
        print(res, entry[1], 'Fail')

print(f'Part 1: {part1(data)}')

print(f'Part 2: {part2(data)}')
