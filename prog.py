x = float(input("Enter value of X : "))
y = float(input("Enter value of Y : "))

if x == y:
    print("X and Y are equal")
    if y != 0:
        print("therefore, x/y is : " + x/y)
elif x < y:
    print("Y is greater than X")
else:
    print("X is greater than Y")

print("Thank you!")