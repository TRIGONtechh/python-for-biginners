# ---in tuple values cant be changed---
# tip = (1,2,3,4,5,6,7,8,9,"python","home",123,345)
# print(tip)
# print("length of  tip",len(tip))

# for i in tip:
#     print(i)

# if 123 in tip:
#     print("yes")

# to change the value in tuple

country = ("spain","germany","india","pakisthan","america")
temp = list(country)
temp.append("russia") # to add items
temp.remove("pakisthan") # to remove items
temp[1]  = "australia" # to replace items
country = tuple(temp)
print(country)

# so here russia is added to country
#  so here pakisthan is rmeoved from country
# so here autralia is replaced with germany in  country
# so here we have changed the value of country
print("\n")
# -----to add touple-----

a = ("pak","ind","aus")
b = ("arje","afr",)
add = a+b
print("here a and b is added:",add)