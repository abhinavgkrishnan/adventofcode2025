from input import ids

def isInvalid (id):
    invalid = False
    idStr = str(id)
    digits = [digit for digit in idStr] 
    for i in range(1,(len(digits)//2)+1):
        if digits[:i] * (len(digits) // i) == digits:
                invalid =True
    return invalid;
    
sum = 0
for i in ids:
    parts = i.split('-')
    for j in range(int(parts[0]),int(parts[1])+1):
        invalid = isInvalid(j)
        if invalid == True:
            sum+=j
print(sum)