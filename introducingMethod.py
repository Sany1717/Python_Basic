'''Introducing Method are three type -> i."Instance_Method"
                                       ii."Class_Method"
                                       iii."Static_Method"'''

class ClassName:
    def InstanceMethod(self):
        print("I love country")
    @ classmethod
    def classMethod(cls):
        print("This is Class_Method")
    @ staticmethod
    def staticMethod():
        print("This is static_Method")
v = ClassName()
v.InstanceMethod()
ClassName.classMethod()
ClassName.staticMethod()