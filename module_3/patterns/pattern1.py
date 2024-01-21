"""
pattern 1:
-------------
* 
* *
* * *
* * * *
* * * * *
"""

# Print pattern as above based on user input
# suppose number is 5 then 5 lines should contains the pattern

number = int(input("Rows for pattern: "))

for i in range(0,number):  # for rows
    for j in range(0,i+1): # fow columns
        print("*",end=" ") # for pattern print
    print()                # for new lines 

# steps:
# input number is 5

# how many rows we required ? 5 = as input parameter is 5
# in each column pattern is incremented by one


# 1st iteration
# i = 0
# j in range(0, 1):
# it will print * once in first row

# 2nd iteration
# i = 1
# j in range(0,2):
# it will print * * in second row for 2 columns 

# 3rd iteration
# i = 2
# j in range(0,3):
# it will print * * * in second row for 3 columns 

# 4th iteration
# i = 3
# j in range(0,4):
# it will print * * * * in second row for 4 columns 

# 5th iteration
# i = 4
# j in range(0,5):
# it will print * * * * * in second row for 5 columns 
    
# Result:
#--------------------
#  Cols | 1 2 3 4 5 |
#-------|------------        
# Row 1 | *         |
# Row 2 | * *       |
# Row 3 | * * *     |
# Row 4 | * * * *   |
# Row 5 | * * * * * |
# -------------------
    
# Assignment 1
# pattern
# -------------
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ---------------
# Solution
# for i in range(0,number):
#     for j in range(0,i+1):
#         print(f"{j+1}",end=" ")
#     print()

    
# Assignment 2
# pattern
# -------------
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# ---------------
# Solution
# for i in range(0,number):
#     for j in range(0,i+1):
#         print(f"{i+1}",end=" ")
#     print()