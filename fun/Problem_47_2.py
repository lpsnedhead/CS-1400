stock = [5, 220, 32, 12, 55, 11, 55 , 117]
f = []
length = len(stock) - 1
length2 = int(len(stock))
count = -1
x = 0
q = 0
for x in range(length2):
    while q < length2:
        while count < (length - x):   
            count += 1
            difference = (stock[length - x] - stock[count])
            f.append(difference)
            q + 1
    x+= 1
#print(f)
'''
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
    '''
#print(f)
f_length = len(f)
#print(f_length)
print(f"The max is {max(f)}")
    
