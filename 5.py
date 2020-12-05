def get_row(entry):
    row = 0
    value = 64
    for char in entry[:7]:
        if char == 'B':
            row += value
        value //= 2
    return row


def get_col(entry):
    col = 0
    value = 4
    for char in entry[7:]:
        if char == 'R':
            col += value
        value //= 2
    return col


def get_id(entry):
    return get_row(entry)*8+get_col(entry)


test_data1 = ['BFFFBBFRRR',
              'FFFBBBFRRR',
              'BBFFBBFRLL']

test_rows1 = [70, 14, 102]
test_cols1 = [7, 7, 4]
test_ids1 = [567, 119, 820]

for i in range(len(test_data1)):
    if get_row(test_data1[i]) != test_rows1[i]:
        print(get_row(test_data1[i]), test_rows1[i])
    if get_col(test_data1[i]) != test_cols1[i]:
        print(get_col(test_data1[i]), test_cols1[i])
    if get_id(test_data1[i]) != test_ids1[i]:
        print(get_id(test_data1[i]), test_ids1[i])

data = [row for row in open('5.txt').read().split('\n') if row]

ids = set(get_id(entry) for entry in data)

print(max(ids))

for i in range(1, 128*8):
    if i-1 in ids and i+1 in ids and i not in ids:
        print(i)
        break
