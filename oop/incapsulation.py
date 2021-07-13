class MySecret:
    def __init__(self):
        self.__private_atr  = 30
        self.__atribute = 0

    def get_private(self):
        return self.__private_atr

    def set_atr(self, value):
        if value < 100:
            self.__private_atr = value

# public atribute
    @property
    def atribute(self):
        return self.__atribute

    @atribute.setter
    def atribute(self, value):
        if value < 100:
            self.__atribute = value


obj = MySecret()
print(obj.get_private())
# print(obj.__private_atr)
print(obj._MySecret__private_atr)
print(obj.set_atr(10))
print(obj.get_private())
print("***********************************")
obj1 = MySecret()
print(obj1.atribute)
obj1.atribute =20
print(obj1.atribute)

