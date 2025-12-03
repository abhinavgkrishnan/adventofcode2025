from input import powerbanks

def largestBattery (battery):
    joltage = 0
    batteryString = str(battery)
    digits = [digit for digit in batteryString]

    for i in range (len(digits)):
        for j in range (i+1,len(digits)):
            current = int(str(digits[i])+str(digits[j]))
            joltage = max(joltage,current)

    return joltage;
    
totalJoltage = 0
for i in range(len(powerbanks)):
    joltage = largestBattery(powerbanks[i])
    totalJoltage+=joltage
print(totalJoltage)