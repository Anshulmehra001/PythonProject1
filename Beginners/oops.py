#print('hello')
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.getSalary
Employee1 = Employee("Employee1","20000")
print(Employee1.salary)
print(Employee1.name)
Employee1.getSalary()

Employee2 = Employee("Employee2","25000")
print(Employee2.salary)
print(Employee2.name)


# Employee2.getSalary()
# Employee1.getSalary()


