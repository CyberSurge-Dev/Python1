import importlib
import os
from inspect import getmembers, isfunction

clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')

folders = [
    "Unit_3",
    "Unit_4",
    "Unit_5",
    "Unit_6",
    "Unit_7_8",
    "Unit_9",
    "Projects"
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
    "alarmclock.py",
    # "Math.py",
    "GuidedPractice2.py",
    "main",
    "Main"
]

for folder in folders:
    for filename in os.listdir(folder):
        if filename.count(".py") >= 1 and filename not in exceptions:
            fn = folder + "." + filename
            print(fn[:-3])

            module = importlib.import_module(fn[:-3])

            Temp_funcs = getmembers(module, isfunction)
            print(Temp_funcs)
            for func in Temp_funcs:
                print(func[0])
                if func[0] not in exceptions:
                    print(func[0])
                    funcs.append(func)

clear()
x = 0
print(" All functions:")
while x < len(funcs):
    x += 1
    print(f"  {x}. {funcs[x - 1][0]}")

input("\n Enter key to exit:")
