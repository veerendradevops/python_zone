Employee = {"Name": "Veerendra", "Age": 29, "salary": 25000, "Company":"GOOGLE"}
print(type(Employee))
print("printing employee data...")
print(Employee)
print("Deleting some of the employee data")
del Employee["Name"]
del Employee["Company"]
print("printing the modified information")
print(Employee)
print
