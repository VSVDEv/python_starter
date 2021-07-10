import sys

# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
# objects - what we print
# sep - separator
# end - what we print after all
# file - file where we print our output
# flush - immediately send file content to buffer

print(2,3,4, sep=',')
print('he', 'llo', sep='')
print(1, end=' ')
print(2, end='\n\n')
print('he', end='')
print('llo')