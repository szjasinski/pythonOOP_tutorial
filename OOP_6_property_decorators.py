

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # we want our email to change if we change the name of our employee
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None



emp_1 = Employee('szmk', 'jasinski', 50_000)

# emp_1.first = 'Jim'
emp_1.fullname = "kcprk braciak"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first)
