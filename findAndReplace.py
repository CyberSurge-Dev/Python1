# Zachary Hoover || Find and Replace
# 11-4-22


import os

folders = [
    "Unit 3",
    "Unit 4",
    "Unit 5",
    "Unit 6",
    "Unit 7-8",
    "Unit 9",
    "Other"
]
find = '# call auto menu function\nautoMenu()'
replace = r'if __name__ == "__main__": autoMenu();'

for folder in folders:
    for filename in os.listdir(folder):
        try:
            with open(f"{folder}/{filename}", 'r') as file :
                filedata = file.read()
            filedata = filedata.replace(find, replace)
            with open(f"{folder}/{filename}", 'w') as file:
                file.write(filedata)
            print(f"{folder}/{filename}")
        except:
            continue
        

print("Done!")

