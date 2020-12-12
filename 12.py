import math

def part1(data):
    ypos = 0.0
    xpos = 0.0
    angle = 90

    for ins in data:
        if ins[0] == 'N':
            ypos += ins[1]
        elif ins[0] == 'S':
            ypos -= ins[1]
        elif ins[0] == 'E':
            xpos += ins[1]
        elif ins[0] == 'W':
            xpos -= ins[1]
        elif ins[0] == 'L':
            angle = (angle - ins[1]) % 360
        elif ins[0] == 'R':
            angle = (angle + ins[1]) % 360
        elif ins[0] == 'F':
            xpos += math.sin(math.radians(angle))*ins[1]
            ypos += math.cos(math.radians(angle))*ins[1]
    return abs(xpos)+abs(ypos)


def part2(data):
    ypos = 0
    xpos = 0
    ygoal = 1
    xgoal= 10

    for ins in data:
        if ins[0] == 'N':
            ygoal += ins[1]
        elif ins[0] == 'S':
            ygoal -= ins[1]
        elif ins[0] == 'E':
            xgoal += ins[1]
        elif ins[0] == 'W':
            xgoal -= ins[1]
        elif ins[0] == 'L':
            if ins[1] == 270:
                tmp = xgoal
                xgoal = ygoal
                ygoal = -tmp
            elif ins[1] == 180:
                xgoal = -xgoal
                ygoal = -ygoal                
            elif ins[1] == 90:
                tmp = xgoal
                xgoal = -ygoal
                ygoal = tmp
        elif ins[0] == 'R':
            if ins[1] == 90:
                tmp = xgoal
                xgoal = ygoal
                ygoal = -tmp
            elif ins[1] == 180:
                xgoal = -xgoal
                ygoal = -ygoal                
            elif ins[1] == 270:
                tmp = xgoal
                xgoal = -ygoal
                ygoal = tmp
        elif ins[0] == 'F':
            xpos += ins[1]*xgoal
            ypos += ins[1]*ygoal
    return abs(xpos)+abs(ypos)

data = [(val[0], int(val[1:])) for val in open('12.txt').read().split('\n') if val]

test_data = [(val[0], int(val[1:])) for val in '''F10
N3
F7
R90
F11'''.split('\n')]

#print(part1(test_data))
#print(part2(test_data))

print(part1(data))
print(part2(data))
