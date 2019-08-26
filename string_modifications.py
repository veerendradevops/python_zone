str= "Hello"
str1= "world"
print(str*3) # prints HelloHelloHello
print(str+str1) # prints Helloworld
print(str[4]) #prints 0
print(str[2:4]) # prints ll
print('w' in str) # prints false as w is not present in str
print('wo' not in str1) #prints false as wo is present in str1
print('rl' in str1) #prints True as rl present in str1
print(r'C://python37') #prints C://python37 as it is written
print("The string str : %s"%(str)) #prints The string str: Hello


#Python Allows us to use the format specifiers used in C's printf statement. The format specifiers in python are treated in the same way as they are treated in C. However, Python provides an additional operator % which is used as an interface between the format specifiers and their values. In other words, we can say that it binds the format specifiers to the values.



Integer = 10;
Float = 1.290
String = "ayush"

print("Hi I am integer ... My value is %d\n Hi I am Float...My value is %f\n Hi I am string ...My value is %s"%(Integer,Float,String));

print(String.capitalize()) # This method changes the 'ayush' as 'Ayush'
str="VEERENDRA"
print(str.casefold()) # It will print veerendra # it requires python3



