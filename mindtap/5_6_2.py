# Python3 Program to convert decimal to  
# given base
def decimalToRep(input_number, base):
    input_number = input_number
    base = base
    def re_value(num): 
      
        if (num >= 0 and num <= 9): 
            return chr(num + ord('0')); 
        else: 
            return chr(num - 10 + ord('A')); 
      
    # reverse a string 
    def strev(str): 
      
        len = len(str); 
        for i in range(int(len / 2)): 
            temp = str[i]; 
            str[i] = str[len - i - 1]; 
            str[len - i - 1] = temp; 
      
    # Function to convert a given decimal  
    # number to a base 
    def from_decimal(res, base, input_number): 
      
        index = 0;  
      
 
        while (input_number > 0): 
            res+= re_value(input_number % base); 
            input_number = int(input_number / base); 
       
        res = res[::-1]; 
      
        return res; 

    res = ""; 
    print(f"{from_decimal(res, base, input_number)}"); 
decimalToRep(10,16)