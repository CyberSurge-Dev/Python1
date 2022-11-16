names =[]

for x in range(1,6):
      print(" Enter the names of 5 of your friends.")
      print(" If you dont have enough friends, or dont have 5")
      print(" you can exit the questions early by typing \'i don't have friends :(\' \n")

      name = input(f" What is the name of friend {x}: ")
      if name == "i don't have friends :(":
        break
      else:
        names.append(name)