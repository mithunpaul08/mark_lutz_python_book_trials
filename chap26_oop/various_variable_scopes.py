
from Employees import Employee


#Employee.setName(Employee,"patti")
print(f"at 1:{Employee._name}")
print(f"at 1.5:{Employee()._name}")
c1=Employee()
print(f"at 1.9:{c1._name}")
c1._name="temp"

print(f"at 2:{c1._name}")
print(f"at 3:{Employee._name}")

c3=Employee
print(f"at 2.5:{c3._name}")


c1.setName("deepa")
print(f"at 4:{c1._name}")
print(f"at 5:{Employee._name}")
c2=Employee()
c2.setName("mithun")
print(c2._name)
print(c1._name)
print(Employee._name)