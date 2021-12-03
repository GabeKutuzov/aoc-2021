# day 1 challenge of AoC

file = open('note.txt', 'r')
lines = file.readlines()


lastsum = 9999
count = 0

isBreak = False

#print(len(lines))

i = 0
for line in lines:

    sum = 0

    if(i + 3 > len(lines)):
        #print("EXIT")
        break
        
    for j in range(3):
        #print(str(i +j))
        sum += int(lines[i + j])

    if(sum > lastsum):
        count += 1

    lastsum = sum

    print(str(sum))
    i += 1


print("Total sum increases: " + str(count));
file.close()
