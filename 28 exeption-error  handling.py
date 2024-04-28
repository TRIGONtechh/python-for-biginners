# use dby try and exept code3
# it help sto skip the error n run the remaining program

a = input("put any number:")
print(f"mul of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("error")


try:
    b = int(input("put any num for an array"))
    ins = [1,3,4]
    print(ins[b])
except ValueError:
    print("error u can only put intiger")
except IndexError:
    print("inproper index")


# if input is string this exept error is run
# try funtion is not implemented


# for i in range(1,11):
#     print(int(a)*i)
