# day 1 challenge of AoC

file = open('note.txt', 'r')
lines = file.readlines()

i = 0
count = 0
last_value = 9999999999;
for line in lines:
    i += 1
    value = int(line)

    if(value > last_value):
        count += 1;

    last_value = value;

    #print("Line: " + str(value))

print(count);
file.close()
