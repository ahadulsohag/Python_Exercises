x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num  # Returns 43
    return x        # Returns 43

def set_global_x(num):
    global x
    x        # Returns 5
    x = num  # global var x is now set to 6
    return x        # Returns 6

print(set_x(43))
print(set_global_x(6))