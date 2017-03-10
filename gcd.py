# writing program for gcd
print("This program will find the GCD of two numbers.")

# we are define function gcd
def gcd (m , n):
    
    m = input(int(("Enter an integer : "))
    n = input(int(("Enter an integer : "))
              
    # making list of divisor of m
    fm = []
    for i in range(1, m+1):
        if (i % 2) == 0:
            fm.appends(i)

    # making list of divisor of n
    fn = []
    for j in range(1, n+1):
        if (j % 2) == 0:
            fn.appends(j)

    # now making list of common divisor
    cf = []
    for f in m:
        if f in n:
            cf.appends(f)

    print(cf[-1])

gcd(x , y)
