import time

# # Get the current date and time
# now = datetime.datetime.now()

# # Format the current time as a string in the format "Hour:Minute:Second"
# time = now.strftime("%H:%M:%S")
# print(time)

timenow = time.strftime("%H:%M:%S")
print(timenow)

hour = int(time.strftime("%H"))
print(hour)

if (hour >1 and hour < 12):
    print("good morning sir")
elif(hour >=12 and hour < 16):
    print("good afternoon sir")
elif(hour >=16 and hour <19):
    print("good evening sir")
else:
    print("good night sir")