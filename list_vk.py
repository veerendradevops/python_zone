emp = ["John",102,"USA"]
Dep1 = ["CS",10]
Dep2 = ["IT",11]
HOD_CS = [10,"veerendra"]
HOD_IT = [11,"Mr.kumar"]
print("printing employee data");
print("Name: %s, ID:%d, Country:%s"%(emp[0],emp[1],emp[2]));
print("printing departments")
print("Deparment 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s,ID: %s"%(Dep1[0],Dep1[1],Dep2[0],Dep2[1]));
print("printing HOD details")
print("CS HOD NAME: %s,id: %d"%(HOD_CS[1],HOD_CS[0]));
print("IT HOD NAME: %s, id: %d"%(HOD_IT[1],HOD_IT[0]));
print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT));
