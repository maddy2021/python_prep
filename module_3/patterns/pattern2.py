"""
pattern 2:
------------- 
* * * * *
* * * *
* * * 
* * 
*
"""

# Print pattern as above based on user input
# suppose number is 5 then 5 lines should contains the pattern

number = int(input("Rows for pattern: "))

for i in range(0,number):  # for rows
    for j in range(number,i,-1): # fow columns
        print("*",end=" ") # for pattern print
    print()                # for new lines 

# steps:
# input number is 5

# how many rows we required ? 5 = as input parameter is 5
# in each column pattern is decremented by one


# 1st iteration
# i = 0
# j in range(5, 0, -1):  here it means it will decrease 1 each time means it will iterate for 5 times
# it will print * * * * * once in first row

# 2nd iteration
# i = 1
# j in range(5, 1, -1):
# it will print * * * * in second row for 4 columns 

# 3rd iteration
# i = 2
# j in range(5, 2, -1):
# it will print * * *  in second row for 3 columns 

# 4th iteration
# i = 3
# j in range(5, 3, -1):
# it will print * * in second row for 2 columns 

# 5th iteration
# i = 4
# j in range(5, 4, -1):
# it will print * in second row for 1 columns 
    
# Result:
#--------------------
#  Cols | 1 2 3 4 5 |
#-------|------------        
# Row 1 | * * * * * |
# Row 2 | * * * *   |
# Row 3 | * * *     |
# Row 4 | * *       |
# Row 5 | *         |
# -------------------
    
# Assignment 1
# pattern
# -------------
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# ---------------
# Solution
# for i in range(0,number):
#     for j in range(number,i,-1):
#         print(f"{j}",end=" ")
#     print()

    
# Assignment 2
# pattern
# -------------
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4 
# 5
# ---------------
# Solution
# for i in range(0,number):
#     for j in range(number,i,-1):
#         print(f"{i+1}",end=" ")
#     print()
    
# Assignment 3
# pattern
# -------------
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2
# 1
# ---------------
# Solution
# for i in range(0,number):
#     count = 0
#     for j in range(number,i,-1):
#         count=count+1
#         print(f"{count}",end=" ")
#     print()

# Assignment 4
# pattern
# -------------
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# ---------------
# Solution
# count = number
# for i in range(0,number):
#     for j in range(number,i,-1):
#         print(f"{count}",end=" ")
#     count = count-1
#     print()
