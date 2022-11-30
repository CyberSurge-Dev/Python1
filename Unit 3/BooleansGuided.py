# Zachary Hoover || Guided Practice #3: Booleans
# 9-28-22


import os
global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def returnMain():
    print("\n press any key to continue")
    input()
    main()
# prints the top header
def printHeader():
    clear()
    print("\n     Boolean guided practice    ")
    print(" --------------+----------------\n")

#prints a bool
def printBool():
    printHeader()
    
    print(True)
    f_bool = False
    print(f_bool)

    returnMain()

# uses .isalpha() to check if a string has letters, prnts boolean
def isAlphaTest():
    printHeader()
    
    message = "lets test out booleans"
    print(message.isalpha())
    print(message)
    print("\n")
    message = "3"
    print(message.isalpha())
    print(message)

    returnMain()
    

# Tests strings to see if they contain letters or numbers
def islnumTest():
    printHeader()
    
    example = "abc 123"
    print(example, " || is alphanumeric? || ", example.isalnum())

    example = "abc_123"
    print(example, " || is alphanumeric? || ", example.isalnum())
    
    example = "000"
    print(example, " || is alphanumeric? || ", example.isalnum())

    example = "aaaa"
    print(example, " || is alphanumeric? || ", example.isalnum())

    returnMain()

# returns if a string is in title case
def istitleTest():
    printHeader()
    
    message = "A Cold Stormy Night"
    print(message, " || is title case? || ", message.istitle())
    message = message.lower()
    print(message, "|| is title case?|| ", message.istitle())

    returnMain()

# checking for digit
def isdigitTest():
    printHeader()
    
    example= "15460"
    print(example)
    print(example.isdigit())
 
    example= "154ayush60"
    print(example)
    print(example.isdigit())

    returnMain()

def islowerisupperTest():
    printHeader()
    
    # checking for uppercase characters
    example= 'GEEKSFORGEEKS'
    print(example)
    print(example.isupper())
    
    example= 'GeeksforGeeks'
    print(example)
    print(example.isupper())

    # checking for lowercase characters
    example= 'geeksforgeeks'
    print(example)
    print(example.islower())
  
    example= 'GeeksforGeeks'
    print(example)
    print(example.islower())

    returnMain()
    
# checks if a string starts with something
def startswithTest():
    printHeader()
    
    # Python code to implement startswith()
    string = "GeeksforGeeks"
    print(string)
    print(str.startswith("Geeks"))

    returnMain()

# main function, and menu
def main():
    bench_mode = False
    
    printHeader()
    print(" Enter number of item")
    print("  1. printBool()")
    print("  2. isAlphaTest()")
    print("  3. islnumTest()")
    print("  4. istitleTest()")
    print("  5. isdigitTest()")
    print("  6. islowerisupperTest()")
    print("  7. startswithTest()")

    userIn = input()

    if userIn == "1":
        printBool()
    elif userIn == "2":
        isAlphaTest()
    elif userIn == "3":
        islnumTest()
    elif userIn == "4":
        istitleTest()
    elif userIn == "5":
        isdigitTest()
    elif userIn == "6":
        islowerisupperTest()
    elif userIn == "6":
        startswithTest()
    else:
        main()
# call main function
if __name__ == "__main__": main()
