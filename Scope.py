'''
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function.

A variable created in the main body of the
Python code is a global variable and belongs to the
global scope.
Global variables are available from within any scope, global and local.
'''
a = 30 # gobal variable
b = 50

def hablu ():
    x = 60 # local variable
    print(x)
    print(a)
hablu()
'''print(x)   not output because this is local variable '''
print(b)