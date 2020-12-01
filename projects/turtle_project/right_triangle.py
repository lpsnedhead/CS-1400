
def main():
    try:
                
        one_side = float(input("Enter the first side: "))
        two_side = float(input("Enter the second side: "))
        third_side = float(input("Enter the third side: "))
       
       
       
       
        if (one_side ** 2) + (two_side ** 2) == (third_side ** 2):
             print("The triangle is a right triangle.")
            return
        
        if (two_side ** 2) + (third_side ** 2) == (one_side ** 2):
            print("The triangle is a right triangle.")
            return
        
        if (one_side ** 2) + (third_side ** 2) == (two_side ** 2):
            print("The triangle is a right triangle.")
            return
        
        else:
            print("The triangle is not a right triangle.")
        
    except ValueError:
        print("Enter postive numbers for lengths")
        return
    
        
if __name__ == "__main__":
    main()