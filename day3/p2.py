import math

file = open('input.txt')
lines = file.readlines()

gr = 0
er = 0

bit = 0
bs = 10000

string = lines[0]
first_num = int(string[0])

index = 0

i = 0

gamma = "" 
epsilon = ""


# 0 -> oxygen; 1 -> c02;
def determine(criteria):

    newlist = lines

    times0 = 0
    times1 = 0

    times0b = 0
    times1b = 0

    for i in range(12):

        if(len(newlist) == 1):
            print(newlist[0])
            break

        stringt = ''

    
        times0 = 0
        times1 = 0

        for line in newlist:
            num = int(line[i]) 
            if(num == 0):
                times0 += 1
            elif(num == 1):
                times1 += 1

        if(i > 0):
            print(str(i))
            print(newlist)
            print("times0, times1 " + str(times0) + " " + str(times1) )

        #print("Im here " + str(times0))
        # recreate list; decide what to keep
        listb = []
        for line in newlist:
            num = int(line[i])

            # Oxygen criteria
            if(criteria == 0):
                if(times0 == times1 and num == 1):
                    listb.append(line)
                    times1b += 1
                elif(times0 > times1 and num == 0):
                    listb.append(line)
                    times0b += 1
                elif(times0 < times1 and num == 1):
                    listb.append(line)
                    times1b += 1
                #print(line)

            # C02 criteria
            elif(criteria == 1):
                if(times0 == times1 and num == 0):
                    listb.append(line)
                    times0b += 1
                elif(times0 > times1 and num == 1):
                    listb.append(line)
                    times1b += 1
                elif(times0 < times1 and num == 0):
                    listb.append(line)
                    times0b += 0

            newlist = listb
        print("next")

    if(len(newlist) == 1):
        print("Complete")
        print(newlist[0])

print("Oxygen")
determine(0)
print("\nC02")
determine(1)

file.close()
