#Python filter() function is used tp get filtered elements. This function takes two arguments, first is a function and the second is iterable. The filter function returns a sequence of those elements of iterable object for which function returns true value

def filterdata(x):
    if x>5:
        return x
    #calling the function
result = filter(filterdata,(1,2,6))
#Displaying result
print(list(result))
