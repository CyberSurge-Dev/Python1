# Zachary Hoover || Find and Replace
# 11-4-22


import os

folders = [
    "Unit 3",
    "Unit 4",
    "Unit 5",
    "Unit 6",
    "Unit 7",
    "Other"
]
find = 'clear = lambda: os.system(\'cls\')'
replace = r'clear = lambda: os.system("clear" if os.name == "posix" else "cls")'

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

