def simple_interest():

    p=float(input("Enter the principal amount?"))
    t=float(input("Enter the time?"))
    r=float(input("Enter the rate? "))
    print("Simple Interest: ",(p*t*r)/100)

simple_interest()

#-----------------calling with parameters--------------------

def simple_interest1(p,t,r):
    return (p*t*r)/100
p= float(input("Enter the pricipal amount?" ))
t= float(input("Enter the time?"))
r= float(input("Enter tha rate of interest"))

print("Simple interest:",simple_interest1(p,t,r))

#------------------providing tge values at the time of calling the function------

def simple_interest3(p,t,r):
    return (p*t*r)/100
print("SimpleInterest is : ",simple_interest3(p=5000,t=10,r=10))






