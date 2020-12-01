def main():    
    starting = float(input("Enter the starting salary: "))
    annual_percent = float(input("Enter the annual % increase: "))
    years = int(input("Enter the number of years: "))
    #salary = float(starting * ((annual_percent / 100 + 1) ** (years - 1)))
    #print(salary)
    salary_list = [] 
    list_year = list(range(0, years))
    for x in list_year:
       salary = (round(starting * ((annual_percent / 100 + 1) ** (x)),2))
       #print(x) 
       salary_list.append(salary)
       #print(f"{x + 1} {salary}")
    print("Year   Salary")
    print("-------------")
    y = 0
    for x in salary_list:
        #print(f"{y + 1}  {salary_list[y]}")
        print("{:<6} {:.2f}".format(y + 1, salary_list[y]))
#         {:.2f}".format(x)

        y = y + 1
    
    
if __name__ == "__main__":
    main()
    