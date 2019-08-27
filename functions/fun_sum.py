# python function to calculate the sum of two variables
#defining the function
def sum(a,b):
    return a+b;

# taking the values from the user
a=int(input("Enter a: "))
b=int(input("Enter b: "))

#calling the function
#print("Sum is ",sum(a,b))
print("Sum is %d+%d=%d"%(a,b,sum(a,b)))

#calling with different values
print("Sum=%d"%(sum(5,6)))
