'''
Project Name: Yondu project
Author: Peyton Sneddon
Due Date: 09/15/2020
Course: CS1400-009

This program calculates the
amount of units each reaver should get.

I learned about Floats vs Int. and
if statements.
'''

def main():
    '''
    Program starts here.
    '''
    
    
    try:
        # (1) replace pass with your code
        reavers = int(input("How many Reavers: "))
        units = int(input("How many units: "))
        leftovers = 0
    
        if reavers < 1 or units < 1:
            print("Enter positive integers for reavers and units.")
            return

        if reavers < 3:
            print("Not enough crew.")
            return

        if units <= 3 * reavers:
            print("Not enough units.")
            return
        
        
        
        units_after_lotus = units - ((reavers - 2) * 3)
        #print("units after lotus " + str(int(units_after_lotus)))
        
        yondu_cut = int(units_after_lotus * .13)
        #print("Yondu's cut = " + str(int(yondu_cut)))
        
        peter_cut = int((units_after_lotus - yondu_cut) * .11)
        #print("peter's cut = " + str(int(peter_cut)))
        
        crew_cut = (units_after_lotus - (peter_cut + yondu_cut)) / reavers
        
        rbf = (units_after_lotus - (peter_cut + yondu_cut)) % reavers
        
        yondu_cut = yondu_cut + crew_cut
        
        peter_cut = peter_cut + crew_cut
        
        #print output
        print("Yondu's share: " + str(int(yondu_cut)))
        print("Peter's share: " + str(int(peter_cut)))
        print("Crew: " + str(int(crew_cut)))
        print("RBF: " + str(int(rbf)))
        
        
    except ValueError:
        print("Enter postive integers for reavers and units.")
        return
    
   
   
    

if __name__ == "__main__":
    main()
    
