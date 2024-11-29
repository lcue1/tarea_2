from Fornitures import Chairs,Table,Bed
# I can create multiple objects from fornitures
def main():
    #Create instance chair
    c=Chairs("Wood",26.98)
    c.getInformationForniture()
    
    #Create instance chair
    tc=Chairs("Metal",130.60)
    c.getInformationForniture()
    
    #Create instance bed
    p=Bed("Plastic",350.60)
    p.getInformationForniture()
    


if(__name__=="__main__"): main()