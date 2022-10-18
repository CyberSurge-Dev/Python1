# Zachary hoover || Boolean Expressions Alarm Clock
# 9-28-22

# One handed clock version 1.0
import time
import os
global clear
clear = lambda: os.system('cls')


current_time = time.localtime( )

hour = current_time.tm_hour
minutes = current_time.tm_min

# print(f"{hour}:{minutes}")

# asks user for the hour
print("what time do you want an alarm?")
print("hour(0-23): ")
hourRequest = int(input())

# check if value is a valid time
if hourRequest > 23:
    print("not within bounds")
    quit()
elif hourRequest < 0:
    print("not within bounds")
    quit()

# asks user for minutes
print("minute(0-60): ")
minuteRequest = int(input())

# check if value is a valid time
if minuteRequest > 60:
    print("not within bounds")
    quit()
elif minuteRequest < 0:
    print("not within bounds")
    quit()

clear()
print(f"{hour}:{minutes}")
while True:
    current_time = time.localtime( )

    hour = current_time.tm_hour
    minutes = current_time.tm_min
    
    prevHour = hour
    prevMin = minutes
    time.sleep(1)

    # code from guided practice, would work if the condition in the second if statement is changed
    # time_to_get_up = hour > hourRequest or (hour == hourRequest and minutes > minuteRequest)
    
    # only prints time if its diffferent from last loop
    if  hour != prevHour and minutes != prevMin:
        clear()
        print(f"{hour}:{minutes}")
        

    # displays "time to get up!" if time request is equal to the current time
    if hourRequest == hour and minuteRequest == minutes:
        clear()
        print(f"{hour}:{minutes}")
        print("time to get up!")





















    





    
