for i in range(5):
    print(i)
else:
    print("no i")
# bcz after 4 no iteratiob
# so else is printed after


# for i in range(5): on;y for 5(== for i in []):

for i in []:
    print(i)
else:
    print("no i")
# else is printed as no iterration
print("\n")


for i in range(6):
    print(i)
    if i == 4:
      break
else:
    print("i is not prnted forword")
# loop is not breaked it is ended here so else is not printed
#  as iteration is stoped at  4

i = 0
while i<6:
    print(i)
    i = i+1
    if i == 4:
     break
    

# loop is not breaked it is ended here so else is not printed
#  as iteration is stoped at  4

for x in range(6):
   print("the iteration {} in for loop".format(x+1))
else:
   print("else block in loop")
print("loop is out")


