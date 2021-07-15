class Base:
    def method(self):
        print("hello!")


class Child(Base):
    pass


class Second(Base):
    def sec(self):
        print("sec method")

    def method(self):
        print("redefined method")


obj = Child()
obj.method()
obj1 = Second()
obj1.method()
obj1.sec()


#####


class Figure:
    def __init__(self, side=0.0):
        self.side = side


class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('*' * self.side)


class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)


def main():
    obj = Square(5)
    obj.draw()
    triangle = Triangle(8)
    triangle.draw()


if __name__ == '__main__':
    main()


# multi inheritance

class Horse:
    def run(self):
        print("I am running")


class Bird:
    def fly(self):
        print("I am flying")


class Pegasus(Horse, Bird):
    pass


def main():
    pegas = Pegasus()
    pegas.run()
    pegas.fly()


# show all parents of Pegasus
print(Pegasus.__bases__)
print(Horse.__bases__)

if __name__ == '__main__':
    main()


class Basic(object):
    def met(self):
        print("method class: ", __class__.__name__)
        print("Instance class:", type(self).__name__)


class Children(Basic):
    pass


if __name__ == '__main__':
    base = Basic()
    base.met()

    child = Children()
    child.met()


# dimond
# __mro__ solver Method Resolution Order

class A:
    def m(self):
        print("A method")
        print("Base ", type(self).__name__)


class B(A):
    pass


class C(A):
    def m(self):
        print("C method")
        print("Child ", type(self).__name__)


class D(B, C):
    pass


class E(A):
    def m(self):
        A.m(self)
        print("Child method invoked on ", type(self).__name__)


class F(A):
    def m(self):
        # super get next in mro after specified
        super(F, self).m()
        # super().m()
        print("Child method invoked on ", type(self).__name__)


obj = D()
obj.m()

for cls in [A, B, C, D]:
    print(cls.__name__ + ":", cls.mro())

# access to base class attributes
obj = A()
obj.m()
obj2 = D()
obj2.m()
print("**************")
A.m(obj2)
C.m(obj)
print("***************")
obj3 = E()
obj3.m()
print("***********")
A.m(obj3)
print("///////////")
E.m(obj)
print("**************")

obj4 = F()
obj4.m()

print(isinstance(obj4, F))
print(isinstance(obj4, A))
print(isinstance(obj4, C))
print(issubclass(obj4, F))
print(issubclass(obj4, A))
print(issubclass(obj4, C))