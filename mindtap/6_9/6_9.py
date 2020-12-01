one_list = []
def list_of_text(one_list):
    new_list = []
    f = open("numbers.txt")
    lines = f.readlines()
    print(lines)
    for value in lines:       
        one_list.append(value.strip())
    for line in one_list:
        x = line.split()
        new_list.append(x)
        
    print(new_list)
    return one_list
    

def calculation(one_list):
    added_sum = (sum(one_list))
    total_numbers = (len(one_list))
    print(one_list)
    #print(added_sum / total_numbers)

list_of_text(one_list)
#calculation(one_list)

#print(one_list)