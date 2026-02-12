import numpy as np

print("hello")
for  i in np.arange(0,10,1):
    if i < 4:
        print(f"{i} is lower than 4")
    else:
        print(f"{i} is higher or equal than 4")
print("great work")