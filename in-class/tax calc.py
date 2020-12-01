STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

def request_inputs():
    grossIncome = float(input("enter the gross income: "))
    numDependents = int(input("enter the number of dependents: "))
    return grossIncome, numDependents

def compute_tax(income, dependents):
    deductions = STANDARD_DEDUCTION + DEPENDENT_DEDUCTION * dependents
    taxableIncome = income - deductions
    incomeTax = taxableIncome * TAX_RATE
    return incomeTax

def print_tax(tax):
    print(f"The income tax is ${tax:,.2f}")
    
def main():
    grossIncome, numDependents = request_inputs()
    incomeTax = compute_tax(grossIncome, numdependents)
    print_tax(incomeTax)
    
main()