def decimal_to_binary(num):
    num = bin(num)[2:]
    print(f"{num} \n")
    
def decimal_to_hex(num):
    num = hex(num)[2:]
    print(f"{num} \n")
    
def decimal_to_octal(num):
    num = oct(num)[2:]
    print(f"{num} \n")
    
def decimal_to_decimal(num): 
    num = num
    print(f"{num} \n")
    
    
    # calls other functions
def decimalToRep(num, base):
    num = num
    if base == 2:
        decimal_to_binary(num)   
        return ''
    if base == 8:
        decimal_to_octal(num)
        return ''
    if base == 16:
        decimal_to_hex(num)
        return ''
    if base == 10:
        decimal_to_decimal(num)
        return ''
def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))
if __name__ == "__main__":
    main()