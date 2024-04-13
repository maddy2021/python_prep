list1 = [6, 7 , 3 , 8, 9 , 15, 12, 10]

max_number = 0
#find max from list
for i in range(len(list1)):
    if max_number<list1[i]:
        max_number = list1[i]

print(f"max number: {max_number}")

import sys
#find min from list
min_number = sys.maxsize
for i in range(len(list1)):
    if min_number>list1[i]:
        min_number = list1[i]

print(f"min number: {min_number}")
