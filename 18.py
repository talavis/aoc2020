def part1(data):
    def part1_recur(current, next_index=1):
        res = 0
        op = '+'
        if next_index == len(data):
            return res, '', next_index
        while next_index < len(data)+1:
            if current[0] == '(':
                if op == '+':
                    tmp, current, next_index = part1_recur(current[1:], next_index)
                    res += tmp
                elif op == '*':
                    tmp, current, next_index = part1_recur(current[1:], next_index)
                    res *= tmp
                if current == '':
                    if next_index == len(data):
                        break
                    current = data[next_index]
                    next_index += 1
                continue

            if current[-1] == ')':
                if current[0] != ')':
                    if op == '+':
                        res += int(current[:current.index(')')])
                    else:
                        res *= int(current[:current.index(')')])
                return res, current[current.index(')'):-1], next_index

            if current in ('+', '*'):
                op = current
            elif op == '+':
                res += int(current)
            else:
                res *= int(current)
            if next_index == len(data):
                break
            current = data[next_index]
            next_index += 1
        return res, '', next_index

    data = data.split(' ')
    return part1_recur(data[0])[0]


def part2(data):
    def recur(ds):
        if not ds:
            return 0

        # parantheses
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
#        print(f'After paranthesis: {ds}')

        # addition
        data = ds.split(' ')
        i = 0
        while i < len(data):
            if data[i] == '+':
                data = data[:i-1] + [str(int(data[i-1]) + int(data[i+1]))] + data[i+2:]
            else:
                i += 1
#        print(f'After addition: {data}')

        # multipiication
        result = 1
        for i in range(0, len(data), 2):
            result *= int(data[i])
#        print(f'After multiplication: {result}')
        return result
    return recur(data)


data = open('18.txt').read().split('\n')

test_data1 = [('1 + 2 * 3 + 4 * 5 + 6', 71),
              ('2 * 3 + (4 * 5)', 26),
              ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)]

for entry in test_data1:
    if (res := part1(entry[0])) != entry[1]:
        print(res, entry[1], 'Fail')

test_data2 = [('1 + 2 * 3 + 4 * 5 + 6', 231),
              ('2 * 3 + (4 * 5)', 46),
              ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340)]

for entry in test_data2:
    if (res := part2(entry[0])) != entry[1]:
        print(res, entry[1], 'Fail')
res = 0
for entry in data:
    res += part1(entry)
print(f'Part 1: {res}')

res = 0
for entry in data:
    res += part2(entry)
print(f'Part 2: {res}')
