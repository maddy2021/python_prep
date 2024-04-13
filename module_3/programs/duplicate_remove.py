list1 = [11, 22 , 33, 44, 11, 22, 99]

# remove duplicate from the list usng another list
new_list = []
for item in list1:
    if item not in new_list:   # if item not in new list then append it in new list #logic to remove duplicate
        new_list.append(item)

print(new_list)
