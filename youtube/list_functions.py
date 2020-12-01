
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "karen", "jim", "oscar", "toby"]

print (friends)

friends.insert(1, "kelly")

print(friends)

friends.append("creed")

print(friends)

friends.extend(lucky_numbers)

print(friends)

friends.remove("jim")

print(friends)

print(friends.index("oscar"))

friends.sort()
print(friends)