plain_text = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""

for ch in plain_text:
    ord_value = ord(ch)
    cipher_value = ord_value + distance
    #print(cipher_value)
    
    if cipher_value > ord('z'):
        cipher_value = ord('a') + distance - \
                       (ord('z') - ord_value +1)
        print("made it .1")
    code += chr(cipher_value)
    #print(f" ciphter value = {chr(cipher_value)} ")
print(f"code = {code}")
    

        