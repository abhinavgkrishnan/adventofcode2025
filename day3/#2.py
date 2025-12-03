from input import powerbanks

def largestBattery (battery):
    joltage = ""
    batteryString = str(battery)
    noOfBatteries= len(batteryString)
    maxbatteries = 12
    currentPos= 0
    totalSelected = 0
    # print(noOfBatteries)
    digits = [digit for digit in batteryString]
    # print(max(digits))
    # print(digits.index(max(digits)))

    for i in range (maxbatteries):
        currentWindowEnd = noOfBatteries - (maxbatteries - totalSelected) + 1
        currentWindow = digits[currentPos:currentWindowEnd]
        # print(currentWindowEnd)
        # print(currentWindow)
        maxIncurrentWindow = max((currentWindow))
        # print(maxIncurrentWindow)
        currentPos += currentWindow.index(maxIncurrentWindow) + 1
        # print(currentPos)
        joltage+=str(maxIncurrentWindow)
        totalSelected+=1

    return int(joltage);
    
totalJoltage = 0
for i in range(len(powerbanks)):
    joltage = largestBattery(powerbanks[i])
    totalJoltage+=joltage
print(totalJoltage)