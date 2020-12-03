area_map = [row for row in open('3.txt').read().split('\n') if row]

row_length = len(area_map[0])

trees1 = 0
x1 = 0

for row in area_map:
    if row[x1] == '#':
        trees1 += 1
    x1 = (x1 + 3) % row_length    
print(trees1)

product = 1

for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    x = 0
    trees = 0
    for y in range(0, len(area_map), slope[1]):
        if area_map[y][x] == '#':
            trees += 1
        x = (x + slope[0]) % row_length
    print(slope, trees)
    product *= trees

print(product)
