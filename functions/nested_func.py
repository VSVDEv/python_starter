# def outher():
#    def inner():
#       print('inner')
#
#     print('other')
#     inner()

def outher():
    def inner():
       print('inner')

    print('other')
    inner()


outher()

# area visible

def funct():
    print(var)

var = "global"
funct()



def funct1():
    var = "local"
    print(var)

var = "global"
funct1()

print(var)


# nested

def outf():
   var = 8

   def inners():
       nonlocal var
       print(var)
       var = 10
   print(var)
   inners()
   print(var)


var = 0
print(var)
outf()
print(var)


# recursive

def nonrecursive(n):
    result = 1
    for multi in range(2, n + 1):
        result *=multi
    return result

def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)


print(nonrecursive(3))
print(recursive(3))