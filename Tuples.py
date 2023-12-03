#tuples..use () <- This is immutable

NewTuple = (1,2,4,5,"eshan","False")
print(type(NewTuple))

#Negative Indexing
print(NewTuple[-2])

#Range of Indexing
print(NewTuple[2:6])

#Update Tuples
ThisTuple = ("Eshan","Hablu","Tutul","Ahad")
a = list(ThisTuple)
a.append("Foysal")
a.insert(2,"Habu")
b = tuple(a)
print(b)

#Unpacking a Tuple
fruits = ("apple", "banana", "cherry", "Gablu")
(a,b,c,d) = fruits
print(b)
print(a)
##Unpacking a Tuple "Another Preoss..(Using Asterisk*)"
(a,*b) = fruits
print(a)
print(b)

#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)
#join tuples
num1 = (1,2,3,4,5)
num2 = (6,7,8,9,10)
print(num1+num2)

#Multiply tuples
Num = ("esu","gupal",420,520)
print(Num*3)

#Tuple method
shopnerRani = ("mahi","porimoni","sabnur","payel","mahi","digi","mahi","mahi")
print(shopnerRani.index("payel"))
print(shopnerRani.count("mahi"))