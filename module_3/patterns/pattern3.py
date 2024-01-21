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

