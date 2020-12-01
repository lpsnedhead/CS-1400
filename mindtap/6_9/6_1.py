# Modify the code below
"""
File: newton.py
Project 6.1

Compute the square root of a number (uses function with loop).

1. The input is a number, or enter/return to halt the
   input process.

2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""
#ret = 1
def newton(x):
    # Initialize the tolerance and estimate
    estimate = 1.0
    tolerance = 0.000001
    ret = 0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        ret = float(estimate)
        #return ret
        if difference <= tolerance:
            break
    #print(ret)
    return ret

def main():
    import math
    # Receive the input number from the user
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == '':
            exit()
        else:
            x = float(x)
            break
    newton(x)

    # Output the result
    print(f"The program's estimate is {newton(x)}")
    print("Python's estimate is", math.sqrt(x))
    
if __name__ == "__main__":
    main()