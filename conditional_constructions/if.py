# if condition:
#       operators
# (NOT RECOMMEND) if condition: operators
# pass - doing nothing

number = int(input('enter number: '))
if number > 5:
    print('this number ' + str(number) + " is greater than 5")

number = int(input('enter number: '))
if number > 5:
    pass

# if condition:
#    do
# else:
#     do

number = int(input('enter number: '))
if number > 5:
    print('greater than 5')
else:
    print('less than 5')

x = float(input('x=  '))
if x > 0:
    y = x ** 0.5
else:
    y = x ** 2
print(y)

# inner if

x = 4
if 0 < x < 7:
    print('value is in the range')
    y = 2 * x - 5
    if y < 0:
        print('negative number')
    else:
        if y > 0:
            print('positive number')
        else:
            print('y=0')



# or and
isredy = True
state = isredy and "Ready" or "Not ready"
print(state)


# ternary
# statement if condition else statement2
state = "Ready" if isredy else "Not ready"
print(state)
print("Ready" if isredy else "Not ready")


# not boolean
string = "10"
if string is not None and string !='':
    num = int(string)

print(num)

if string:
    num = int(string)

print(num)