# def func_name(param):
# //dodo

def print_numbers(limit):
    for i in range(limit):
        print(i)


n = int(input('n= '))
print_numbers(n)


# def name_func(a,b):
#    return a + b

def sum(first, second):
    return first + second


print("**********************")
print(sum(2, 3))


# if only return -> mean return None

def say_hello():
    print("Hello!!!")


say_hello()


# modules
# if__name__=="__main__":
# main()


def info_print(object_name, color, price):
    print('Object: ', object_name, sep='\t')
    print('Color: ', color, sep='\t')
    print('Price: ', price, sep='\t')
    print()


info_print('pen', 'blue', '1')
info_print(object_name='ppp', color='yellow', price=2)
info_print(price=4, object_name='pen', color='dark')
info_print('pen', price=3, color='grey')


# you cannot do this or order or names if change order it won`t works
# info_print(price=4, 'pen', 'blue')

# optional parameters

def hi(name='alex'):
    print('hello, ', name, '!', sep='')


hi()

name = "sam"
hi(name)
