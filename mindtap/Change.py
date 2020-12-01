cost = float(input("enter cost: "))
paid = float(input("enter amount paid: "))
change = (paid - cost)
print(change)
if change < 0:
    print("insufficient funds")
