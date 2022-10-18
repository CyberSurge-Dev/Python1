import os


#cr function
def cr(num):
    global houndreds
    global fifties
    global twenties
    global tens
    global fives
    global ones

    houndreds = 0
    fifties = 0
    twenties = 0
    tens = 0
    ones = 0
    fives = 0

    #cylce houndreds
    while num >= 100:
        if num < 100:
            break
        num -= 100
        houndreds += 1

    #cylce fifties
    while num >= 50:
        if num < 50:
            break
        num -= 50
        fifties += 1

    #cylce Tenties    
    while num >= 20:
        if num < 20:
            break
        num -= 20
        twenties += 1

    #cylce Tens    
    while num >= 10:
        if num < 10:
            break
        num -= 10
        tens += 1

    #cylce fives    
    while num >= 5:
        if num < 5:
            break
        num -= 5
        fives += 1

    #cylce ones    
    while num >= 1:
        if num < 1:
            break
        num -= 1
        ones += 1
    return num

os.system('cls' if os.name == 'nt' else 'clear')

print("Input a number: ")
x = input()

extra = cr(float(x))

print("houndreds: " + str(houndreds))
print("fifties: " + str(fifties))
print("twenties: " + str(twenties))
print("tens: " + str(tens))
print("fives: " + str(fives))
print("ones: " + str(ones))
print("extra: " + str(round(extra, 2)))












        
