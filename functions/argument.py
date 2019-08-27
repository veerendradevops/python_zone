# the argument name is the required argument to the function func
def func(name):
    message = "Hi" +name;
    return message;
#name = str(input("Enter the name?")) # we need to run it by using python3
name = str(raw_input("Enter the name?")) # we need to run it by using python2
print(func(name))

