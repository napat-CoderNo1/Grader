# creating a new dictionary
my_dict ={"Java":100, "Python":112, "C":11}

x = list(my_dict.keys())
y = list(my_dict.values())

print(x)
print(y)

print(x[y.index(100)])

# one-liner
# print("One line Code Key value: ", list(my_dict.keys()) [list(my_dict.values()).index(100)])