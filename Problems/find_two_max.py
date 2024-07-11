
def get_two_max(a,b,c):
    highest, second_highest = 0, 0
    
    if a > b and a > c:
        highest = a
        if b > c:
            second_highest = b
        else:
            second_highest = c

    elif b > a and b > c:
        highest = b
        if a > c:
            second_highest = a
        else:
            second_highest = c

    elif c > a and c > b:
        highest = c
        if a > b:
            second_highest = a
        else:
            second_highest = b

    return highest, second_highest

print(get_two_max(3,1,2))