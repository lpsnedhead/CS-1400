'''
[111,101,100]
[100,111,101]
'''

def shift_right():
    new_string = input("Enter a string of bits: ")
    bin_list = []
    new_list = []
    # create string in bin
    for ch in new_string:
        ord_value = ord(ch)
        bin_char = bin(ord_value)
        
        bin_list.append(bin_char)
    #print(bin_list)
    # shift right
    message_length = len(bin_list)     

    new_list.append(bin_list[message_length - 1])
    #print(f"new list = {new_list}")
    count = 0
    
    while count < (len(bin_list) - 1):
        new_list.append(bin_list[count])
        count = count + 1
    # convert to string
    shifted_string = ""
    for bin_ch in new_list:
        shifted_string += chr(int(bin_ch,2))
    print(f"shifted string = {shifted_string}")
    
    
'''
[111,101,100,1001,1100]
[1100,111]
'''

def left_shift():
    new_string = input("Enter a string of bits: ")
    bin_list = []
    new_list = []
    # create string in bin
    for ch in new_string:
        ord_value = ord(ch)
        bin_char = bin(ord_value)
        
        bin_list.append(bin_char)
    #print(bin_list)
    # shift right
    message_length = len(bin_list)     

    new_list.append(bin_list[0])
    #print(f"new list = {new_list}")
    count = message_length - 1
    
    while count > 0:
        new_list.insert(0, bin_list[count])
        count = count - 1
    print(new_list)    
    # convert to string
    shifted_string = ""
    for bin_ch in new_list:
        shifted_string += chr(int(bin_ch,2))
    print(f"shifted string = {shifted_string}")
def main():
    shift_right()
    
if __name__ == "__main__":
    main()
    