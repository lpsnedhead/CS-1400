wage = float(input("Enter the wage: $"))
hours = int(input("Enter the regular hours: "))
overtime = int(input("Enter the overtime hours: "))
normal_pay = wage * hours
over_pay = wage * 1.5 * overtime
print(f"${normal_pay + over_pay}")
