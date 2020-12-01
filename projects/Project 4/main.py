import csv
import pathlib

symbol_pos = 0
date_pos = 1
price_pos = 2

def file_checker():
    
    file = pathlib.Path("stocks_data.csv")
    x = 0
    while x == 0:
        if file.exists():
            x += 1
        else:
            print("file stocks_data.csv does not exist")
            exit()
            
            
def get_symbol_list(data, symbols):
   # list of symbols:
    for line in data:
        symbol = line[symbol_pos]
        if "symbol".lower() in symbol.lower():
            continue
        match = symbol in symbols
        if match == False:
            symbols.append(symbol)
    return symbols

def output_summary_data(summary_data):
    #print(f"SYMBOL DATA {summary_data}")
    for stock in summary_data:
     print(stock[0])
     print("----")
     print(f"Max: {stock[3]} {stock[4]}")
     print(f"Min: {stock[1]} {stock[2]}")
     print(f"Ave: {stock[5]}")
     print("\n")
     
def write_to_file(summary_data):
    f = open("stock_summary.txt", "w+")
    for stock in summary_data:
     f.write(f"{stock[0]} \n")
     f.write("----\n")
     f.write(f"Max: {stock[3]} {stock[4]}\n")
     f.write(f"Min: {stock[1]} {stock[2]}\n")
     f.write(f"Ave: {stock[5]}\n")
     f.write("\n")

def output_high_low(max_symbol, max_date, stock_max, min_symbol, min_date, stock_min):
    print(f"Highest: {max_symbol}, {max_date}, {stock_max}")    
    print(f"Lowest: {min_symbol}, {min_date}, {stock_min}")



def main():
    file_checker()
    f = open("stocks_data.csv")
    lines = f.readlines()
    f.close
    data = []
    symbols = []
    symbol_data = []
    stock_results = []

    for line in lines:
        
        symbol = ''
        date = ''
        close = ''
        line = line.strip(" \ufeff")
        line
        values = line.split(',')
        data.append(values)
    #print(data)

    get_symbol_list(data, symbols)
    # min max and average
    #print(f"SYMBOLS ARE:{symbols}")
    for symbol in symbols:
        #print(symbol) 
        stock_min = 0.0
        min_date = ''
        stock_max = 0.0
        max_date = ''
        stock_average = 0.0
        number_of_stock = 0
        stock_price_total = 0.0
        
        first_row_instance = True
        
        
        
        for row in data:

            if symbol != row[symbol_pos]:
                continue
            
            # check if max
            if float(stock_max) <= float(row[price_pos]):
                stock_max = row[price_pos]
                max_date = row[date_pos]
                
                
                
            #check if min
            if first_row_instance == True:
                stock_min = float(row[price_pos])
                min_date = row[date_pos]
                first_row_instance = False
                
            elif float(stock_min) > float(row[price_pos]):
                stock_min = row[price_pos]
                min_date = row[date_pos]
                
            #average info
            number_of_stock += 1
            stock_price_total += float(row[price_pos])
            
        stock_average = stock_price_total / number_of_stock
        
        symbol_data.append([symbol.rstrip("\n"), str(stock_min).rstrip("\n"), str(min_date).rstrip("\n"), str(stock_max).rstrip("\n"), max_date.rstrip("\n"), str(stock_average).rstrip("\n")])
        #print(f"{symbol} Max = {stock_max} on {max_date},MIN = {stock_min} on {min_date},AVERAGE = {stock_average}")
        #print(f"AVG: {stock_price_total} / {number_of_stock} = {stock_average}")
        #    print(number_of_stock)
    #print(symbol_data)
        

    stock_max = 0.0
    max_date = ''
    min_symbol = ''
    stock_min = 0.0
    min_date = ''
    min_symbol = ''
    max_symbol = ''
    first_row_instance = True
    for row in symbol_data:
        #print(row)
        if stock_max < float(row[3]):
            stock_max = float(row[3])
            max_date = row[4]
            max_symbol = row[0]
            
        if first_row_instance == True:
            stock_min = float(row[1])
            min_date = row[2]
            min_symbol = row[0]
            first_row_instance = False
            
        elif stock_min > float(row[1]):
            min_symbol = row[0]
            stock_min = row[1]
            min_date = row[2]
            #print("changed")
        #print(f" IN LOOP MIN {min_symbol}, {min_date}, {stock_min}")
    #print(f" LOOK HERE MAX {max_symbol}, {max_date}, {stock_max}")    
    #print(f" LOOK HERE MIN {min_symbol}, {min_date}, {stock_min}")
    output_summary_data(symbol_data)
    write_to_file(symbol_data)
    output_high_low(max_symbol, max_date, stock_max, min_symbol, min_date, stock_min)
if __name__ == "__main__":
    main()
