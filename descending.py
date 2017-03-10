def descending(m):
    #statement
    l = len(m)
    if (l == 0):
        return True
    else:
        t = 1
        for i in range(0,l):
            if (m[i] <= m[i+1]):
                t = t + 1
                if (t == l-1):
                    return True
            else:
                return False
        if(t==l):
            return True

x = []
y = [4,4,3]
z = [19,17,18,7]
print(descending(z))