num_1 = 4
num_2 = 56
print("This is supper number is",num_1+num_2)
# another pross.......
print(f"this is supper number is {num_2+num_1}")

user_name = "eshan"
roll = 40
print(f"My name is {user_name} and my class roll {roll}")

'''Binary type data...
2 type binary__1.bytes(this is immutable)
                2.bytearray(this is mutable)
                range=(0-255) 2 type bytes'''

hablu_list = [1,3,4,5,6,7,8]
b = bytes(hablu_list)
print(type(b))
print(hablu_list)
#Bytesarray...
x = [4,5,6,7,8,9]
x1 = bytearray(x)
print(type(x1))
print(x)
x1[1]=100 #changing value...
print(x1[1])

#None type data....
y = None
print(type(y))

'''sequence type data.
    There are 3 type:1.list(mutable), 2.tuple(immutable), 3.range'''
#list type data..
li = ['cat','dog','cow','chiken']
print(type(li))
li[2]="lion" #changing....
print(li[2])

#tuple type data.
tup = (3,4,5,6,7)
print(type(tup))
print(tup)
#range type data...
ran = range(5)
print(ran)
#example:\
for i in ran:
    print(i)