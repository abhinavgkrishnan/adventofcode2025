from input import ids

def isInvalid (id):
    invalid = False
    idStr = str(id)
    mid = len(idStr)//2
    if idStr[:mid] == idStr[mid:]:
        invalid = True
    return invalid;


sum = 0

for i in ids:
    parts = i.split('-')
    for j in range(int(parts[0]),int(parts[1])+1):
        invalid = isInvalid(j)
        if invalid == True:
            sum+=j
print(sum)