class vehicle:
    def __init__(self,model,brand,component):
        self.model = model
        self.brand = brand
        self.component = component
class plane(vehicle):
    pass
class car(vehicle):
    pass
class bike(vehicle):
    pass

p = plane("k20", "bangladesh airlince", "stil")
c = car("bazzaz", "GX r", "etoment")
b = bike("rx100", "roel enifinit", "others")

print(p.brand,p.model,p.component)
print(c.component,c.brand,c.model)
print(b.component,b.brand,c.model)