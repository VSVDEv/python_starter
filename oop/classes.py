class MyClass:
    int_field = 5
    str_field = 'a string'


print(MyClass.str_field)
print(MyClass.int_field)

obj1 = MyClass()
obj2 = MyClass()

print(obj1.int_field)
print(obj2.str_field)

MyClass.int_field = 10
print(MyClass.int_field)
print(obj1.int_field)

# only this object change in class and obj2 no changes
obj1.str_field = "another"
print(MyClass.str_field)
print(obj1.str_field)
print(obj2.str_field)


class Person:
    pass


joe = Person()
joe.name = "Joe"
joe.age = 30
print(joe.name + " " + str(joe.age))


class PersonWithInfo:
    # init constructor work first when initiate class after creating object of class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


joe = PersonWithInfo("Tom", 30)
# we cannot do that because of __init__
# joe.name = "Joe"
# joe.age = 30
print(joe.name + " " + str(joe.age))
joe.print_info()
