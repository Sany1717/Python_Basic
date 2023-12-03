#Sets....."{},unoder"
Myset = {1,2,3,"esu","ali",5}
print(type(Myset))
print(Myset)
print(len(Myset))

#Access Set Items
thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)
#Another Prosss....
print("banana" in thisset)

#Add set Items..
Myset_1 = {"Esu","hablu","tutul"}
print(Myset_1)
Myset_1.add("shakil")
print(Myset_1)

#Set update....<- iterable object(tuple,list,dictonares etc)
myset = {"Foyal","Rifat","Ratul","Kolshi"}
print(myset)
set ={4,5,6}
myset.update(set)
print(myset)
list_0 = [0,9,8]
print(type(list_0))
myset.update(list_0)
print(myset)

#Remove Set Items...<- two type method : remove() or discard() method
myset_0 = {1,2,3,4,5,6}
print(myset_0)
myset_0.remove(4)
print(myset_0)
#discard method().......<-Error thro kre na.
myset_00 ={0,9,8,7}
myset_00.discard(10)
print(myset_00)
myset_00.pop()
print(myset_00)
myset_00.clear()
print(myset_00)

#Loop sets
Thisset = {"apple", "banana", "cherry"}
for x in Thisset:
    print(x)

#join Sets <-two typs:Union, update
set_1 = {"a","b","c"}
set_2 = {1,2,3}
set_3 = set_1.union(set_2)
print(set_3)
set_2.update(set_1)
print(set_2)
