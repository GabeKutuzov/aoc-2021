import math

file = open('input.txt')
lines = file.readlines()

gr = 0
er = 0

bit = 0
bs = 10000

string = lines[0]
first_num = int(string[0])
print(first_num)

index = 0

i = 0

gamma = "" 
epsilon = ""


for i in range(12):

    times0 = 0 
    times1 = 0

    stringt = ''

    #print(str(i))
    
    for line in lines:
        num = int(line[i]) 
        if(num == 0):
            times0 += 1
        elif(num == 1):
            times1 += 1

    
    if(times0 > times1):
        gamma+=str(1) 
        epsilon+=str(0)
    elif(times1 > times0):
        gamma+=str(0)
        epsilon+=str(1)

print("Gamma:" + gamma)
print("Epsilon:" + epsilon)


