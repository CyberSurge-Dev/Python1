# Zachary Hoover || Code Analysis: Loops pt 2
# 11-4-22

# get the range the user wants a times table of
def main():
    cycles1 = int(input(" Enter start vlue for table: "))
    cycles2 = int(input(" Enter end value for table: "))

    # get the times_table that the user wants
    times_value = int(input(" Enter a multplication value: "))
    
    # cycle throuh and print the times table for the users values
    for x in range(cycles1, cycles2+1):
        print(f" {x} x {times_value} = {x * times_value}")

    # calls function again
    main()
    
main()
