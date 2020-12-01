code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plain_text = ""
for ch in code:
    ord_value = ord(ch)
    cipher_value = ord_value - distance
    if cipher_value < ord('a'):
        print("test1")
        cipher_value = ord('z') - \
            distance - (ord('a') - ord_value - 1 )
        # 122 - (1 - (97 - 97 - 1 ))
        #print("test2")
        #print((cipher_value))
    plain_text += chr(cipher_value)
print(plain_text)