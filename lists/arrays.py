int_list = [1, 2, 3, 4, 5]
char_list = ['a', 'b', 'c']
empty_list = []

print('numb ', int_list)
print('chars', char_list)
print('empty', empty_list)

list_from_range = list(range(5))
print('range', list_from_range)

list_from_str = list("a string")
print('from string', list_from_str)

my_list = [5, 6, 7, 8, 9, 0]
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# new_list = my_list[start:end:step]

new_list = my_list[1:4:2]
print(new_list)
newest_list = my_list[0:5]
print(newest_list)
new1_list = my_list[1:-2]
print(new1_list)
print(my_list[1:-1])
print(my_list[::-1])
# check list contains
print(8 in my_list)
# quantity of elements
print(len(my_list))

# add
my_list.append(4)
my_list.append(3)
print(my_list)

# remove

del my_list[-1]
print(my_list)

# update

my_list[-1] = 10
print(my_list)

# for

for elem in my_list:
    print(elem)

# fibonacci

n = 10
fibs = [1, 1]
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])

print(fibs)
