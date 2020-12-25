def part1(data):
    divider = 20201227
    val = 7
    loops = 0
    while val != data[0]:
        loops += 1
        val = (val*7) % divider
    key = data[1]
    for i in range(loops):
        key = (key*data[1]) % divider
    return key


test_data = (5764801, 17807724)

print(f'Test for part 1 passed: {part1(test_data) == 14897079}')

data = (1526110, 20175123)

print(part1(data))
