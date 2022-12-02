import time

current_time = time.localtime()

hour = current_time.tm_hour
minutes = current_time.tm_min

#time_to_get_up = hour>6
#print(time_to_get_up)

time_to_get_up = hour > 7 or (hour == 7 and minutes > 53)

print(time_to_get_up)
if time_to_get_up:
    print(f"{hour}:{minutes}")
    print("time to get up!")
    


