# Put your code here
def decimalToRep(num, base): 
    """ 
    Converts given number num, from base 10 to base base  
 
    num = the number in base 10 
    base = base to convert 
    """ 
    assert(num >= 0) 
    assert(1< base < 37) 
    r = '' 
    import string 
    while num > 0: 
        r = string.printable[num % base] + r
        num //= base
    print(r)
    return r

# A main for testing your program
def main():
    
    """Tests the function."""
    (decimalToRep(10, 10))
    (decimalToRep(10, 8))
    (decimalToRep(10, 2))
    (decimalToRep(10, 16))
    
    
    
# The entry point for program enumecution
if __name__ == "__main__":
    main()
