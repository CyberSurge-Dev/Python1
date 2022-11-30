import os
from inspect import getmembers, isfunction


folders = [
	"Unit 3",
	"Unit 4",
	"Unit 5",
	"Unit 6",
    "Unit 7-8",
    "Unit 9",
    "Projects",
    "Other",
]

funcs = []
files = []

exceptions = [
      "autoMenu",
      "printHeader",
      "getmembers",
      "clear",
      "time",
      "isfunction",
      "returnMain",
      "cls",
    ]

for folder in folders:
    for filename in os.listdir(folder):
        if filename.count(".py") <= 1: 
            # files.append(filename)
            fn = filename[:-3]
            foo = __import__("baseTemplate")
            Temp_funcs = getmembers(foo, isfunction)
            for func in Temp_funcs:
                print(func[0])
                if func[0] not in exceptions:
                    funcs.append(func)
                    print(func[0])

x = 0
i = 1
print(" All functions:")
while i < len(funcs):
      if funcs[i][0] not in exceptions:
        x += 1
        print(f"  {x}. {funcs[i][0]}")
      i += 1



