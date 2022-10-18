# Zachary Hoove || Create Formated File v1.0
# 10-17-22

from fileinput import filename
import shutil
from datetime import datetime

template = r'C:\Users\zhoover2891\Downloads\python\baseTemplate.py'

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
filedata2 = filedata.replace('{assignmentName}', AssignmentName)
filedata3 = filedata.replace('# import {moduleName} as foo', f"import {fileName} as foo")

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)
  file.write(filedata2)
  file.write(filedata3)