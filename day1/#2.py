from input import rotation_data
from collections import deque

dial_values = list(range(100))
dial = deque(dial_values)
dial.rotate(-50)
is_zero = False
zero_count = 0

for item in rotation_data :
    if item.startswith("R"):
        for i in range(int(item[1:])):
            dial.rotate(-1)
            if dial[0] == 0:
                zero_count+=1
    elif item.startswith("L"):
        for i in range(int(item[1:])):
            dial.rotate(1)
            if dial[0] == 0:
                zero_count+=1

print(zero_count)