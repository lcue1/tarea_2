class Employer:#Basic class
    def __init__(self, name):
        #atribbues
        self.name=name
        self.salary=465
    #Basic functions
    def calc_salary(self, ):
        return self.salary
    #Get data about employer
    def show_information_employer(self):
        print("****************************************************\n")
        print(f'Employer name: {self.name}\n  Salary: {self.salary}$')

class Mqnanger(Employer):#Extends from Employer
    def __init__(self, name):
        super().__init__(name)
        self.salary=2000# set Mananger salary
    def calc_salary(self, over_time, bono):#Calulate salary
        over_time=(self.salary/160)*over_time
        self.salary= self.salary+over_time+bono
#Asistent employer similar to Mananger only change salary and calculator salary function
class Assistent(Employer):
    def __init__(self, name):
        super().__init__(name)
        self.salary=800
    def calc_salary(self, over_time):
        over_time=(self.salary/160)*over_time
        self.salary= self.salary+over_time