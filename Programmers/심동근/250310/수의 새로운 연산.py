
def find_XY(val):
    if (val == 1):
        return (1, 1)
    elif (val == 2):
        return (1, 2)
    elif (val == 3):
        return (2, 1)



    current_x= 1
    current_y= 1
    lst= [1, 2]
    n= 3

    while(True):
        a_n= lst[-1]+(n-1)
        lst.append(a_n)
        n+=1
        if(val<a_n):





## main ###
val= 8
print(find_XY(val))