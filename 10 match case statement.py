# here match is used for take out particular output 

x = int(input("write any integer value:"))

match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")

    case _:
        print("Greater than 5")

# case statement with if-conditon

# y = int(input("write any 2nd integer value:"))
 
# match y:

#   case _ if y!=90:
#     print("not equal to 90")    
#   case _ if y != 80:
#     print("not equal to 80")
#   case _ :
#      print(y)

# exanmple 2

z = int(input("enter any value: "))

print(z)

match z:
    case _ if x > 5:
      print("z is greater than 5")
    case _ if x <= 5:
      print("z is 5 or less")
    case _:
        ("0")
    
