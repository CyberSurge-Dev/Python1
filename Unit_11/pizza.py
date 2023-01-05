# Zachary Hoover || Guided Practice #31
# 01-04-23

def make_pizza(size, *toppings):
    """"Summarize the pizza we are about to make"""
    print(f"\n Making a {size} - inch pizza with the following toppings:")

    for topping in toppings:
        print(" ", topping)
