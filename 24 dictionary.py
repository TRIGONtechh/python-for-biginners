# dictiniany is used to store given value in keys/variable/value pairs
# "keys":"value"

dic= {"name":"yashash","class":13,"canvote":True}
print(dic)
print(dic["name"])
# print(dic["yashash"])---thrw a error it gives only values not keys

print("get",dic.get(13))
# none(bcz it gives keys vlaues)

print("get class",dic.get("class"))
# 13

print("get keys",dic.keys())
# name,class,canvote

print("get values",dic.values())
#  yashash,13,True

for i in dic.keys():
    print("for keys",i)
# name,class,canvote

for p in dic.values():
    print("for value",p)
for r in dic.keys():
    print("for value dic[p]",dic[r])
# yashash,13,true

print("items",dic.items())
# dict_items([('name', 'yashash'), ('class', 13), ('canvote', True)])
# here we get whole dictionary

for x in dic.keys():
  print(f"value of {x} is {dic[x]}")
# value of name is yashash
# value of class is 13
# value of canvote is True