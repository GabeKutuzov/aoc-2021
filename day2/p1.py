import re

f = 0
u = 0
d = 0

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

    if("up" in str(line)):
        depth -= val
        aim -= val
    if("down" in str(line)):
        depth += val
        aim += val

print(horizontal * depth)
