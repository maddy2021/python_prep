# pattern3:
# -----------------
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# ------------------

print("\n\npattren:3")

number = int(input("Rows for pattern: "))

for i in range(0,number):
    for j in range(0,i+1):
        print("*", end=" ")
    print()
for i in range(0,number-1):
    for j in range(number-1,i,-1):
        print("*", end=" ")
    print()


print("\n\npattren:4")

# pattern 4
# ------------------
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# -----------------
    
for i in range(0,number):
    for k in range(0,i):
        print(" ",end="")
    for j in range(number,i,-1):
        print("*",end=' ')
    print()


print("\n\npattren:5")
# pattern 5
# ------------------
#     *
#    * *
#   * * *
#  * * * * 
# * * * * *
# -----------------
    
for i in range(0,number):
    for k in range(number,i+1,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end=' ')
    print()

print("\n\npattren:6")
# Pattern 6
# ------------------
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#     *
#    * *
#   * * *
#  * * * * 
# * * * * *
# --------------------
for i in range(0,number):
    for k in range(0,i):
        print(" ",end="")
    for j in range(number,i,-1):
        print("*",end=' ')
    print()
for i in range(0,number):
    for k in range(number,i+1,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end=' ')
    print()


print("\n\npattren:7")
# Pattern 7
# ------------------
#     *
#    * *
#   * * *
#  * * * * 
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# ---------
for i in range(0,number):
    for k in range(number,i,-1):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=' ')
    print()
for i in range(0,number):
    for k in range(0,i):
        print(" ",end="")
    for j in range(number,i,-1):
        print("*",end=' ')
    print()




# **********
#     **   
#     **
#     **
#     **
#     **
# ******

# row1: 10
# row 2: 2 : 5,6
# row 6: same

# row 7: 6 star

rows_length=7
print("number of rows: {rows_length}")


cols_length=10
print("number of cols: {cols_length}")


mid_col_number = cols_length//2
mid_row_number = rows_length//4 + 1

print("pattern of letter")
for row in range(0,rows_length):
    for col in range(0,cols_length):
        if row==0:
            print("*",end="")
        if row>0 and row<rows_length-1:
            if(col==mid_col_number-1 or col==mid_col_number):
                print("*",end="")
            else:
                print(" ",end="")
        if(row==rows_length-1):
            if(col<mid_col_number + 1):
                print("*",end="")
            print("",end="")
    print()

# print("pattern of letter")
# for row in range(0,rows_length):
#     for col in range(0,cols_length):
#         if(row>0 and row<mid_row_number):
#             print
#         else:
#             if(col==0 or col==1 or col==cols_length-2 or col==cols_length-3):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     print()


# **     **
# ***   *** 
# **** ****
# *** * ***
# **     **
# **     **
# **     **