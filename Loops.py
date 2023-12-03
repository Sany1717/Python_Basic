#for loop ->for loop is when the number os iteration is alrady known.
#While loop->Whlile loop is when the number os iteration is alrady unknown.

#While loop........
hablu = 0

while hablu <= 10:
    print(hablu,"Yes hablu is less than 10")
    hablu+=1


#For loop....
fruits = ["apple","banana","cherry"]

for n in fruits:
    if n == "banana":
        break
    print(n)