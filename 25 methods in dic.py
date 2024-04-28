dict1 = {123:34,234:90,233:23}
dict2 = {113:45,134:89,133:98}

print(dict1)
# {123: 34, 234: 90, 233: 23}

# to add two dictionary
dict1.update(dict2)
print(dict1)
# {123: 34, 234: 90, 233: 23, 113: 45, 134: 89, 133: 98}

# to delet entire dictionary
# dict1.delete()
# print(dict1)
# throw an error no object


# to remove last elemet from dictionary (.popitems)
dict1.popitem()
print(dict1)
# {123: 34, 234: 90, 233: 23, 113: 45, 134: 89

# to clear delet all the element in the dic
dict1.clear()
print(dict1)
# {}

# to check if a key is present in the dictionary
print(123 in dict1)
# True

# to check if a key is not present in the dictionary
print(123 not in dict1)
# False

# to check if a value is present in the dictionary
print(90 in dict1.values())
# True

# to check if a value is not present in the dictionary
print(90 not in dict1.values())
# False

# to check if a key is present in the dictionary
print(123 in dict1.keys())
# True

# to check if a key is not present in the dictionary
print(123 not in dict1.keys())
# False

# to check if a key is present in the dictionary
print(123 in dict1.items())
# True
