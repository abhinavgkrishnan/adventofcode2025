from input import rotation_data

inital_dial_pos = 50
is_zero = False
zero_count = 0
current_pos = inital_dial_pos

for item in rotation_data :
    if item.startswith("R"):
        current_pos+=int(item[1:])
        if current_pos >= 100:
            current_pos = current_pos % 100
        if current_pos == 0:
            zero_count+=1
    elif item.startswith("L"):
        current_pos-=int(item[1:])
        if current_pos < 0:
            current_pos = current_pos % 100
        if current_pos == 0:
            zero_count+=1

print(zero_count)