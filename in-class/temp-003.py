def c2f(c):
    return 9/5*c + 32

def f2c(f):
    return 5/9*(f-32)

def c2k(c):
    return c + 273.15

def k2c(k):
    return c - 273.15

def f2k(f):
    return c2k(f2c(f))

def k2f(k):
    return c2f(k2c(k))

def main():
    which = input("Which conversion? ")
    t = float(input("Temperature? "))
    
    if which == "c2f":
        f = c2f(t)
        c = t
        print(f"{t} C is {f:,.3f} F.")
    
    elif which == "f2c":
        c = f2c(t)
        print(f"{t} F is {c:,.3f} C.")
    else:
        print("Not valid.")
        return
    
    
    if c < 10:
        print("Cold")
    elif 10 < c <=29:
        print("warm")
    else:
        print("Hot")

if __name__ == "__main__":
    main()