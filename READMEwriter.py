# Zachary Hoover || README writer v1.0
# 10-18-22

import os
files = r"README.md"

folders = [
	"Unit 3",
	"Unit 4",
	"Unit 5",
	"Unit 6",
    "Unit 7",
    "Unit 8",
    "Projects",
    "Other",
    
        
]

lines = []
lines.append("# Python 1\n")
lines.append("Python 1 Academy Honors repo\n")
lines.append("This repo contains ll of the python files from my python 1 class\n")
lines.append("# These are the required steps to replicate the baseTemplate.py file\n")
lines.append(" - Download baseTemplate.py and createFile.py.\n")
lines.append(" - Place the files in the same directory.\n")
lines.append(" - Run createFile, and enter the correct information.\n")

lines.append("# Files listed by unit\n")


for x in folders:
    lines.append("### " + x + "\n")
    # print("1")
    for filename in os.listdir(x):
        lines.append(" - " + filename + "\n")
        # print("2")
    lines.append("\n")

with open(files, "w") as file:
   file.writelines(lines)
   file.close()

print("done")
