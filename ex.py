print('%10s'%('test',))
print('{:>10}'.format('test'))
test2 = "schoooooool"
test1 = "umbrellaaaa"
test0 = "elephantttt"

print(f'{test2:3.93}, {test1:5.2}, {test0:2.1}') # Returns "tes       , te   , t "

print('{:6d}'.format(42))
print('{:+f}'.format(55))
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42) )# Returns "int: 42;  hex: 2a;  oct: 52;  bin: 101010'"
bin_43 = "{0:b}".format(43)
bid = "{0:b}".format(43) 

print(bid)
print(bin_43)
print('{:,}'.format(1234567890))