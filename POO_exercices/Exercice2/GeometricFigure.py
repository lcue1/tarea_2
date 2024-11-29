from abc import ABC, abstractmethod
#Create interface that has two methos 
class CalculeArea(ABC):
    @abstractmethod
    def getArea(self):
        pass
    def showArea(self):
        pass

class Square(CalculeArea):#Implement interface
    def __init__(self,base,height):
        super().__init__()
        self.area=None
        self.base=base
        self.height= height
    
    def getArea(self):#Implement method an calc a rectangle area
        self.area=self.base*self.height

    def showArea(self):#Print a rectangle area
        print(f"The rectangle area is: {self.area}")

class Triangle(CalculeArea):#Implement interface
    def __init__(self,base, height):
        super().__init__()
        self.area=None
        self.base=base
        self.height=height

    def getArea(self):#Implement method an calc a rectangle area
        self.area=self.base*self.height/2

    def showArea(self):#Print a rectangle area
        print(f"The triangle area is: {self.area}")
