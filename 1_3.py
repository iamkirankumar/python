# Program in def funtion()

def computepay(hour,rate):
    try:
        if hour >= 0:
            try:
                if hour > 40:
                    pay = (40*rate) + (hour - 40)*1.5*rate
                elif hour <= 40:
                    pay = hour*rate
                print pay
            except:
                print 'Error! Please enter numeric input!'
        else:
            print 'Hour never in negetive ! Please try again'
    except:
        print 'Error! Please enter numeric input!'
hour = float(input('Enter hours : '))
rate = float(input('Enter rate : '))
computepay(hour,rate)