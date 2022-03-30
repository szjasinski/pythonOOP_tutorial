# OOP PYtHON


# class Employee:
#     pass
#
#
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)
#
# emp_1.first = 'szmk'
# emp_1.last = 'jasinski'
# emp_1.email = 'blabla@gmail.com'
# emp_1.pay = 50_000
#
# emp_2.first = 'wef'
# emp_2.last = 'erverv3w'
# emp_2.email = 'blarevebla@gmail.com'
# emp_2.pay = 90_000
#
# print(emp_1.pay)


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company/com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('szmk', 'jasinski', 50_000)
emp_2 = Employee('kcprk', 'jasinski', 69_000)

print(emp_1)
print(emp_2)

print(emp_1.pay)
print(emp_2.pay)

emp_1.fullname()
Employee.fullname(emp_1)

print(emp_1.fullname())
print(Employee.fullname(emp_1))




