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

number = int(input("Rows for pattern: "))

for i in range(0,number):
    for j in range(0,i+1):
        print("*", end=" ")
    print()
for i in range(0,number-1):
    for j in range(number-1,i,-1):
        print("*", end=" ")
    print()

