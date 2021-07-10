string1 = 'String'
string2 = "String"
print(string1 == string2)
print(string1 is string2)

string3 = "First line. "\
    "second line."
print(string3)

string4 = "First line.  \
          Second line."
print(string4)

string5 = "First line. \n" \
          "Second line."
print(string5)

string6 = "First line. \\" \
          "Second line."
print(string6)

multiline_string = """ Lesson1. Some text djsajkd;salkddsal;jdkl;sajkd;lsad;l
-a
-b
-c"""
print(multiline_string)

string7 = "hello "
string8 = "world !"
print(string7+string8)
print(string7[1])
print('Number = %d' % 17)
print('Float = %f' % 17.2)
print('Float = %4.2f' % 17.2)

# '%s = d%' % ('number', 42)

print('number= {}'.format(17))
print('num = {}'.format(17.3))
print('number = {:5.2f}'.format(17.3))
print('{} = {}'.format('num',42))
print('{1} = {0}'.format('num', 42))