# Zachary Hoove || Create Formated File v1.0
# 10-17-22

import shutil
from datetime import datetime

template = r'baseTemplate.py'

print("\n    File Creator")
print(" --------+---------   \n")
fileName = input(" Enter the name of the file: ")
AssignmentName = input(" Enter the assignment title: ")
path = input(" Enter file path(leave blank for current dir): ")

if path == "":
    path = (fileName + ".py")

shutil.copyfile(template, path)


with open(path, 'r') as file :
  filedata = file.read()

date = datetime.today().strftime('%m-%d-%y')
# Replace the target string
filedata = filedata.replace('{date}', date)
filedata = filedata.replace('{assignmentName}', AssignmentName)
filedata = filedata.replace('# import {moduleName} as foo', f"import {fileName} as foo")
filedata = filedata.replace('# {list = getmembers(foo, isfunction)}', "list = getmembers(foo, isfunction)")

header = r"\n    " + AssignmentName + r"   "
filedata = filedata.replace('{assignmentTitle}', header)
bottom = r" "

i = 0
while i < (len(header)/2):
	bottom += r"-"
	i += 1
bottom += r"+"
i = 0
while i < (len(header)/2):
	bottom += r"-"
	i += 1

bottom += r"\n"

filedata = filedata.replace('{dashThing}', bottom)

# Write the file out again
with open(path, 'w') as file:
  file.write(filedata)
