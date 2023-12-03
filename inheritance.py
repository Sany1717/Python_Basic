'''
parent -> class is the begin inherited from,
also called base class

child class -> is the class that inherits from,
 another class, also called derived class
'''

class baba:
    car = "BMW"
    tk = "10 crore"
    home = "10 floor"
class kaka(baba):
    brokernphone = "1 floor"
    brokernhome = ""
k = kaka()
print(k.home)
print(k.car)
print(k.brokernphone)