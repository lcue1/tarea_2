class Fornitures:#Define a tather class
    def __init__(self, material, price):
        #Atributes
        self.name=material
        self.price=price
    
    def getInformationForniture(self):
        print(f"name {self.name}\n Peice {self.price}")
    
class Chairs(Fornitures):#Hinerence
    def __init__(self, material, price):
        super().__init__(material, price)

class Table(Fornitures):#Hinerence
    def __init__(self, material, price):
        super().__init__(material, price)

class Bed(Fornitures):#Hinerence
    def __init__(self, material, price):
        super().__init__(material, price)

