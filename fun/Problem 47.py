stock = [20, 15, 32, 12, 55, 11]
f = []
length = len(stock) - 1

count = -1
while count < length:   
    count += 1
    difference = (stock[length] - stock[count])
    f.append(difference)
#print(f)

count = -1  
while count < (length - 1):   
    count += 1
    difference = (stock[length - 1] - stock[count])
    f.append(difference)
#print(f)

count = -1  
while count < (length - 2):   
    count += 1
    difference = (stock[length - 2] - stock[count])
    f.append(difference) 
#print(f)

count = -1  
while count < (length - 3):   
    
    count += 1
    difference = (stock[length - 3] - stock[count])
    f.append(difference)
#print(f)

while count < (length - 4):   
    
    count += 1
    difference = (stock[length - 4] - stock[count])
    f.append(difference)
#print(f)
f_length = len(f)
#print(f_length)
print(f"The max is {max(f)}")
    