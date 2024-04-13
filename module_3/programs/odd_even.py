list1 = [10, 11, 12, 14, 19, 20, 55]

# create two list 
# one list should contains odd number and another list should have even number
odd_list =[]
even_list =[]

for number in list1:
    if number%2==0:
        even_list.append(number)
    else:
        odd_list.append(number)

print(f"odd list: {odd_list}")
print(f"evenlist: {even_list}")
