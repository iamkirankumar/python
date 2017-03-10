#Comperision Program

x = float(input('Enter number for X : '))
y = float(input('Enter number for y : '))

if x == y:
    print('X is equal to Y')
    if x !=0:
        print('therefore, x/y is ',x/y)
elif x < y:
    print('X is smaller than Y')
else :
    print('Y is smaller than x')
print('Thanks!')