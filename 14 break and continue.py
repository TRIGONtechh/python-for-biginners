for  i in range(11):
    print("5 *",i,"=",5*i)
# 5 * 0 = 0 is also includedsoo

print("\n")

for i in range(15):
    print("5 *",i+1,"=",5*(i+1))
    if ((i+1)==10):
        break
# -----here loop is brek at 10 intead of 15----

print("\n")

# ---continue is used to skip given n run the rest of the loop----


for i in range(15):
    print("5 *",i+1,"=",5*(i+1))
    if ((i+1)==10):
        continue
print("\n")
for i in range(15):
    if ((i+1)==10):
       continue
    print("5 *",i+1,"=",5*(i+1))