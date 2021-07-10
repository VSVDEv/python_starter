# for variable in range(end_value):
#     operators

# for variable in range(start_value, end_value):
#     operators

# for variable in range(start_value, end_value, step):
#     operators

for i in range(10):
    print("i= ", str(i))

for i in range(3, 10):
    print('i= ' + str(i))

for i in range(0, 10, 2):
    print("i= " + str(i))

for i in range(0, 10, 2):
    if i == 4:
        continue
    print("i= " + str(i))

for i in range(0, 10, 2):
    if i == 4:
        break
    print("i= " + str(i))