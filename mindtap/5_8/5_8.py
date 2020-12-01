'''
Read words from file
split on whitespace into a list
count the words in the list
make a list of unique words
print word counts in alphabetical order
'''
name = input("enter text file name: ")
f = open(name)
text = f.read()
f.close()

words = text.split()

d = { }
for word in words:
    count = d.get(word, 0)
    count += 1
    d[word] = count

keys = list(d.keys())
keys.sort()

for word in keys:
    print(word, d[word])

    