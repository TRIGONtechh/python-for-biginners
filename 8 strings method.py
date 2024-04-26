# here  are some of the tags can be use in python for formatting


a = "yashash ravi"
print(a.upper())
print(a.lower())

b = "!!!! hello brother how r u!!!!!!!"
print(b)
print(b.strip("!"))
print(b.replace("hello", "hi"))
print(b.split(" "))

c= "hi guys i am programming py"
print(c.capitalize())

print(c.center(59))
print(c.count("am"))
print(c.count("i"))

print("\n",c.endswith("py"))
print(c.endswith("am"))
print(c.startswith("hi"))
print(c.find("am"))

str1= "he is very honest man in the world"
print(str1.find("is"))
# print(str1.index("iss"))--throw an error
str2= "Welcomephython"
print(str2.isalnum())
print(str2.isalpha())

str3= "Welcomepyhton 3"
print(str3.isalnum())
print(str3.isalpha())

str3= "Welcome 2 pyhton"
print(str3.isalnum())
print(str3.isalpha())
# isalnum has a-z,A-Z,0-9
# isalpha has a-z,A-Z   but no numbers

exa = "hi yashash \n how r u"
print(exa)
print(exa.isprintable())
# bcz of \n wch is not printable but consolled by phython
op= "     "
print(op.isspace())

til = "introduction to planet"
print(til)
print(til.istitle())
print(til.swapcase())
print("cap as title:::",til.title())








