import re

file = open('input.txt')
lines = file.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:

    tmp = re.findall(r'\d+', line)
    res = list(map(int, tmp))
    val = res[0]

    print(line)
    print(val)

    if("forward" in str(line)):
        horizontal += val
        depth += aim * val

    if("up" in str(line)):
        aim -= val
    if("down" in str(line)):
        aim += val

print(horizontal * depth)
