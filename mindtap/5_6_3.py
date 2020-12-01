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








def decimalToRep(num, base):
    if base == 2:
        bin_num = bin(num)[2:]
        print(f"{bin_num} \n")
        #return bin_num
    if base == 8:
        oct_num = oct(num)[2:]
        print(f"{oct_num} \n")
        #return oct_num
    if base == 16:
        hex_num = hex(num)[2:]
        print(f"{hex_num} \n")
        #return hex_num
    if base == 10:
        dec = base
        print(dec)
        #return dec
def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))
if __name__ == "__main__":
    main()