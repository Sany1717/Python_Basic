#Use objtect method
class parentInfo:
    def RubamasFamily(self,name,age):
        print(f"My name is {name} & my age is {age}")
p1 = parentInfo()
p1.RubamasFamily("Rubama Chowdhury",21)


#Parameterized constructor
class myInfo:
    def __init__(self,name,number):
        print(f"My name is {name} & my number is {number}")

x = myInfo("SANY Bro", "01346865")