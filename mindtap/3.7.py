starting_salary = float(input("Enter the starting salary: "))
annual_increase = float(input("Enter the annual % increase: ")) /100
years = int(input("Enter the number of years: "))
bonus = (years-1) * annual_increase
pay = starting_salary + bonus
total = pay + starting_salary
print(f"{total}")