user_input = input("Enter your Age ")

print("\n")
try:
    val = int(user_input)
    print("Input is an integer number. Number = ", val)
except ValueError:
    try:
        val = float(user_input)
        print("Input is a float  number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")