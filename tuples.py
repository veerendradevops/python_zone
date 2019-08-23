# tuple is used to store the sequence of immutable python objects
x=(1,2,3,4,5)
print(type(x)) # it returnss type of x

# the elements of the set cannt be duplicate
Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Friday"}
Days2 = {"Friday","Saturday","Sunday","Monday"}

print(Days1.intersection(Days2)) #prints the intersection of the two sets
print(Days1)
print(Days2)

Days1.intersection_update(Days2) #remove the items from the original set that are not present in the both the sets
print(Days1)
print(Days2)
