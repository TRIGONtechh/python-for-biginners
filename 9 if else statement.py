# in if else satement we write 3 types
# if,elif,else,
# if,if-else,if-else-elif,nested if-else-elif

age = int(input("Type your age: "))
print(age)
if age <= 18:
    print("you are not eligible to vote")
else:
    print("you are eligible to vote")

# conditional operator --- >,<,<=,>=,==,!=,<=,>=,is,is not,in,not in

# another example
a = int(input("Enter any num: "))
print(a)
if a < 0:
    print("negative")
elif a > 0:
    print("positive")
elif a == 15:
    print("special num")
else:
    print("zero")

# nested if statement

b = int(input("Enter any num: "))
print(b)
if b < 0:
    print("negative")
elif b > 0 and b < 10:
    print("num id btn 0-10")
elif b > 10 and b <20:
    print("num id btn 10-20")
elif b > 20 and b <= 30:
    print("num id btn 20-30")
elif b > 30:
    print("positive")
else:
    print("0")
