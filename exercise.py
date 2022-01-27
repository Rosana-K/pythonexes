hour =input('Enter Hours:   ')
rate =input('Enter Rate:    ')
a = 1.5
if float(hour) > 40:
    pay=float(hour)*float(rate)+(float(hour)-40)*float(rate)*1.5
    print('pay: ',pay )
    #print('Pay {}'.format(float(hour)*float((rate)+1.5)))
else:
    print('Pay {}'.format(float(hour) *float(rate)))
