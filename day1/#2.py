from input import rotation_data

is_zero = False
zero_count = 0
current_pos = 50

for item in rotation_data :
    if item.startswith("R"):
        increment = int(item[1:])
        current_pos+=increment
        full_rotation = current_pos//100
        zero_count+=full_rotation
        current_pos = current_pos % 100
    elif item.startswith("L"):
        decrement = int(item[1:])
        start = current_pos
        current_pos-=decrement
        full_rotation = (current_pos-1)//100
        zero_count+= (start-1)//100 - (full_rotation)
        current_pos = current_pos % 100
            
print(zero_count)