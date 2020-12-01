plain_text = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plain_text:
    ord_value = ord(ch)
    cipher_value = ord_value + distance
    if cipher_value > ord('z'):
        cipher_value = ord('a') + distance - \
                       (ord('z') - ord_value +1)
        code += chr(cipher_value)
print(code)
    

        