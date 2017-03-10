x = input("enter a number you find cube root : ")

ans = 0

while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + " is not a perfect cube root")
else:
    print("Cube root of " + str(x) + " is " + str(ans))