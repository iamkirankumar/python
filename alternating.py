def alternating(l):
    for i in range(len(l)-2):
        if (l[i] < l[i+1]) and (l[i+1] > l[i+2]):
            print(i)
            continue
        if (l[i] > l[i+1]) and (l[i+1] < l[i+2]):
            print(i)
            continue
        return False
    return True

#assigning value to the variable
x = []
y = [1,3,2,3,1,5]
z = [3,2,3,1,5]
x1 = [3,2,2,1,5]
y1 = [3,2,1,3,5]
alternating(y)