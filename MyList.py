#List......this is changeable / use[]
li = [4,5,6,7]
print(li)
li[0]=70
print(li[0]) #change valu index 0 , before 4 and now 70

#Access list Items
gablu = ["youtube","www.com","whats app","facebook"]
print(gablu[3])
#change list item
gablu[2] = "massanger"
print(gablu)

'''Add list item:Two types item= 1.Apped item(last). 2.Insert item(user deside)'''
#apped item
habib = [40,50,500]
habib.append(1)
print(habib)
#insert item
habib.insert(1,100)
print(habib)

#Remove List Itmes:There are 4 type--
#The remove() method removes the specified item.
NewList = ["hablu","bablu","kablu",450,600]
print(NewList)
NewList.remove("kablu")
print(NewList)
#The pop() method removes the specified index.
NewList.pop(3)
print(NewList)
#The del keyword also removes the specified index:
del NewList[1]
print(NewList)
#The clear() method empties the list.
NewList.clear()
print(NewList)

#LoopList
#You can loop through the list items by using a for loop:
LoopList = ["lion","tiger","dog","cat","cow"]
for w in LoopList:
    print(w)

#Use the range() and len() functions to create a suitable iterable.
for v in range(len(LoopList)):
    print(v)
#Print all items, using a while loop to go through all the index numbers
k = 0
while k < len(LoopList):
    print(LoopList[k])
    k = k+1

#list comprehensions.(Double)
p = [1,2,3,4,5]
for n in p:
    print(n*2)
q = [n*3 for n in p]
print(q)

##Sort list.
Num = [4,5,7,9,2,3]
Num.sort()
print(Num)
##Revers list...
a = [1,2,3,4,5]
a.sort(reverse=True)
print(a)
#copy list.
b = [123, 345, 456, 578]
b1 = b.copy()
print(b1)

##Join list....
sum1 =[1,2,3]
sum2 = [3,4,5]
sum1.extend(sum2)
print(sum1)
