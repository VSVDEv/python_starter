number1 = "15"
number2 = int(number1)
print(type(number1))
print(type(number2))
# inherit Int
# 1
boolean = True
# 0
boolean1 = False

print(type(boolean))
print(type(boolean1))

float1 = 2.12
float2 = 4.132
print(float1)
print(type(float1))

# Complex
# Wrong 5-j
# OK
same = ((5 - 1j) == complex(5, -1))
print(same)
complex("5-1j")
same1 = ((5 + 1j) == complex(5, 1))
print(same1)
complex("5+1j")
