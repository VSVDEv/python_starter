# if condition:
#     operator
# elif condition:
#      operator
# else:
#     operator

x = 4
if 0 < x < 7:
    print('value is in the range')
    y = 2 * x - 5
    if y < 0:
        print('negative number')
    elif y > 0:
        print('positive number')
    else:
        print('y=0')

choice = input('enter choice')
if choice == "1":
    print("1")
elif choice == "2":
    print("2")
elif choice == "3":
    print("3")
else:
    print("invalid input")
