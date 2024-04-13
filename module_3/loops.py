# # for loop to print first 100 numbers
# print("for loop example")
# for number in range(1,101):
#     print(number, end=",")

# print("\n\n")

# # while loop to print
# print("while loop example")
# number = 1
# while number<=100:
#     print(number, end=',')
#     number += 1

# print("\n\n")



list1 = [10, 20, 30, 40, 5, 6, 7, 8, 9, 10]

#1st way : using index
# for idx in range(0,len(list1)):
#     if idx==5 or idx==7:
#         print(list1[idx])

#for each
# for item in list1:
#     index = list1.index(item)
#     if index==5 or index==7:
#         print(item**2)

# print("for loop with list using index")
# list1 = [10, 20, 30, 40, 5, 6, 7, 8, 9, 10]
# ## iterate list elements using index
# for index in range(0,len(list1)):
#     print(f"index: {index} value: {list1[index]}")

# print("for each loop with list ")
# ## iterate values using for each 
# for item in list1:
#     print(f"value: {item}")

# ## same goes for tuples

# print("\nfor loop on set")
# # Set : only for each loop will work as indexes is not supported in sets
# set1 = {10,20,30}    
# for item in set1:
#     print(f"value: {item}")


# # iterate items for dictionary
my_dict = {
    "name" : "xyz",
    "phn_num" : 92472386467,
    "email_id" : "xyzgmail.com",
    "hobbies" : ["sports", "music", "movies"]
}

print("\niterate over key value pairs")
for key, value in my_dict.items():
    print(f"key: {key}, value:{value}")


# print("\niterate over keys")
# for key in my_dict.keys():
#     print(f"key: {key}")

# print("\niterate over values")
# for value in my_dict.values():
#     print(f"value:{value}")

