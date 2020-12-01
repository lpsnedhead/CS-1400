def main():
    
    name_of_file = (input("File Name : "))
    f = open(name_of_file, "r")
    counter = 0
    user_number = 0
    x = 0
    num = 3
    f_content = f.read()
# amount of lines in file
    for i in f_content:
        if i == "\n":
            counter += 1
    print(f"The file has {counter} lines.")
    f.close()
#enter a line    
    while x == 0:
        user_number = input("Enter a line number [0 to exit]: ")
        user_number = int(user_number)
    
        if user_number == 0:
            exit()
        if counter >= user_number > 0:
            break
        elif user_number > counter or user_number < 0:
            print(f"ERROR: line number must be less than {(counter)}")
            continue
        
# print wanted line        
    with open(name_of_file) as f:
        i = 1
        for line in f:
            if i == user_number:
                break
            
        i += 1
    print(line)
     
    
if __name__ == "__main__":
    main()