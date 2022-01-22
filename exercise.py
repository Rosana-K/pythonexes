'''hour =input('Enter Hours:   ')
rate =input('Enter Rate:    ')
a = 1.5
if float(hour) > 40:
    print('Pay {}'.format(float((hour)+a) *float(rate)))
else:
    print('Pay {}'.format(float(hour) *float(rate)))'''
score = input('Enter Score:  ')
s=float(score)
if s>=0.9 and s<10.0:
    print("score is A")
elif s>=0.8 and s<0.9:
    print("score is B")
elif s>=0.7 and s<0.8:
    print("score is C")
elif s>=0.6 and s<0.7:
    print("score is D")
elif s<0.6 and s>=0.0:
    print("scors is F")
else:
    print("Error")
