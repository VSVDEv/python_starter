# while condition:
#     operators
response = ""
while response != "exit":
    response = input("type exit to exit: ")

n = 1
while n <= 3:
    print("n: " + str(n))
    n += 1

while True:
    response = input('Enter command')
    if response == 'exit':
        break

x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print('current value equals ', str(x))
    print('(but 5 we don`t print)')


# while condition:
#       block operators
# else:
#      block operators

attempts = 3
while attempts > 0:
    attempts -= 1
    password = input('enter password: ')
    if password == "a":
        print("Logged")
        break
else:
    print("denied")