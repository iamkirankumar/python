# Basic Computation

hour = float(input('Enter hour : '))
if hour >= 0:
    rate = float(input('Enter rate : '))
    pay = hour*rate
    print 'Pay ', pay
else:
    print 'Hour never be negetive'