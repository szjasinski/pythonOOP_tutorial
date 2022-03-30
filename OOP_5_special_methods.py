# double underscores are called Dunder


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # methods changing how our objects are printed and displayed
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # creating method, so adding employees will result in a sum of their total salaries
    def __add__(self, other):
        return self.pay + other.pay

    # another
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('szmk', 'jasinski', 50_000)
emp_2 = Employee('kcprk', 'jasinski', 69_000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

# we can customize how addition works for our objects by creating Dunder add method  # operators overloading
print(1+2)
print(int.__add__(1, 2))
print(str.__add__('1', '2'))

# adding instances of employees
print(emp_1+emp_2)

####
print(len('test'))
print(len(emp_1))
