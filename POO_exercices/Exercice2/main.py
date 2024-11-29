from GeometricFigure import Square, Triangle

def main():
    square = Square(5,4)#Create object
    #Call metods implemented for the object
    square.getArea()
    square.showArea()
    #Second object
    triangle = Triangle(5,4)#Create object
    #Call metods implemented for the object
    triangle.getArea()
    triangle.showArea()

if(__name__=="__main__"): main()