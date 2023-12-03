class baba:
    smart_phone = "google pixcl"
    home = "10 corore"
    tk = "10 floor"
class son_1(baba):
    smartphone = "Iphone"
    Watch = "smartWhatch"
    Ac = "Walton"
class son_2(son_1):
    Webcam = "Fifine K0"
    Laptop = "Hp"
    camara = "Canon"
class son_3(son_2):
    brokern_phone = ""
    brokern_Home = ""

k = son_2()
print(k.smart_phone)
print(k.Ac)