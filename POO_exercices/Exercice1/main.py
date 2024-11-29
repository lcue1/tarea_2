from Employer import Employer,Mqnanger,Assistent\
#This code use POO to calculate salary about an meployer
# I use inherense
def main():
    simpleEmployer=Employer("Juan Perez")#This object don't have bono and extra time
    simpleEmployer.calc_salary()#Calculate salary
    simpleEmployer.show_information_employer()#Show data

    mEmployer = Mqnanger("Julia Sanchez")# Have complete beefist
    mEmployer.calc_salary(3,200)#Calc 3 hours over time and bonus
    mEmployer.show_information_employer()#Show data
    

    #Employer that only have overtime
    aEmployer = Assistent("Rafael Suarez")# Only have over time
    aEmployer.calc_salary(3)#Calc 3 hours over time and bonus
    aEmployer.show_information_employer()#Show data


if(__name__=="__main__"):
    main()
