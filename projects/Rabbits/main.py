'''
[month adult babies total]
   [0     1     0      1]
   [1     1     1      2]
   [2     2     1      3]
   [3     3     2      5]
'''
rabbits = [[1,1,0,1]]
#month = month + 1
month = 0
#adult = previous_baby + previous_adult
adult = 1
#baby = fibonacci
baby = 0
#total = baby + adult
total = 0

#cages = 500

def fibonacci(num_sequence):
    
    
    fib_sequence = []
    fib_previous_two = 0
    fib_number = 0
    fib_previous_one = 0
    #handle first 2 sequences
    fib_sequence.append(0)
    print(fib_number, end=", ")
    fib_number += 1
    fib_sequence.append(fib_number)
    print(fib_number, end=",  ")
    
    
    for _ in range(0,num_sequence):
        fib_previous_two = fib_previous_one
        fib_previous_one = fib_number
        fib_number += fib_previous_two
        print(fib_number, end=", ")
        fib_sequence.append(fib_number)
    print(f"\n{fib_sequence}")
    
    
    
    
def rabbit_reproduction():
    '''
1. seed array with month 0
2. increase month
3. babies
4. adults
5. total
6. cages



rabbits = [[1,1,0,1]]
#month = month + 1
month = 0
#adult = previous_baby + previous_adult
adult = 1
#babies = fibonacci
baby = 0
#total = baby + adult
total = 0

    '''
    print(rabbits[0])  
    #month one
    month_col = 0
    adult_col = 1
    babies_col = 2
    
    
    new_month = rabbits[0][month_col] + 1
    new_babies = rabbits[0][babies_col] + 1
    new_adults = rabbits [0][adult_col] + rabbits [0][babies_col]
    new_total = new_adults + new_babies
    new_months_data = [new_month, new_adults, new_babies, new_total]
    rabbits.append(new_months_data)
    print(f"rabbits = {rabbits}")
    
    
    
    while new_total < 500:
        new_month = rabbits[len(rabbits)-1][month_col] + 1
        new_babies += rabbits[len(rabbits)-2][babies_col]
        new_adults = rabbits[len(rabbits)-1][babies_col] + rabbits[len(rabbits)-1][adult_col]
        new_total = new_adults + new_babies
        rabbits.append([new_month,new_adults,new_babies,new_total])
      
    print(f"---\n {rabbits}")
    
def main ():
    #print(rabbits)    
    #fibonacci(10)
    rabbit_reproduction()
    
    
    

if __name__ == "__main__":
    main()
        