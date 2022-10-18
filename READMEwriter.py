# Zachary Hoovr || README writer v1.0
# 10-18-22

import os
file = r"README.md"

folders = [
	"Unit 3",
	"Unit 4",
	"Unit 5",
	"Unit 6",
	"Other"
]
lines = []
lines.append("")
for x in folders:

	for filename in os.listdir(x):


with open("file.txt", "w") as file:
   file.writelines(lines)
   file.close()