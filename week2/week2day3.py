from unittest import result


def display_twice(name):
    print(name)
    print(name)
#display_twice('Su Su')
def muliple(a):
    return a*5
m=muliple(5)
#print(m)
def muliplication(x,y):
    return x*y
def divided (x,y):
    return x/y
def addition (x,y):
    return x+y
f=addition(2,7)
r=muliplication(2,7)
t=muliple(2)
e=divided(10,2)
#print("addition", f)
#print("muliplication", r)
#print("muliple" , t)
#print("divided", e)
def payment(hour,rate):
    pay=hour*rate
    return pay
p=payment(5,20)
#print("payment is ", p)
def count_child(child1,child2,child3):
    print("The youngest child is ", child3)
#count_child("Su Su", "Mya Mya","Maung Maung")
#count_child(child1="Su Su",child2="Mya Mya",child3="Maung Maung")
def select_color(*color):
    print("The brightest color is ", color[1])
#select_color("brown","red","pink")
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        result=num*factorial(num-1)
        return result
f=factorial(8)
print("the factorial is ", f)






