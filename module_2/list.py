#----------------------------------------------------------------------------------------
# Add single element to list
my_list = [5, 6 ,7 ,12 , 10]
my_list.append(3)
print(my_list)

#------------------------------------------------------------------------------------------
my_list = [5, 6 ,7 ,12 , 10]
# add multiple elements (from an iterable - list tuple string)  to the end of the list. 
my_list.extend([8,4])
print(my_list)

#-------------------------------------------------------------------------------------------
# Difference between extend and append
# append to add single value, extend to add multiple value(like merge)

my_list = [5, 6 ,7 ,12 , 10]
my_list.append([55,22,33])    # =>  [5, 6, 7, 12, 10, [55, 22, 33]] => Treat list as single item and added list inside list
print(my_list)

my_list = [5, 6 ,7 ,12 , 10] 
my_list.extend([55,22,33])    # =>   [5, 6, 7, 12, 10, 55, 22, 33] => Treat list as iterable and merge with the previous list
print(my_list)

#-----------------------------------------------------------------------------------------------
# Adds an element at the specified position

my_list=[5, 6 ,7 ,12 , 10]
my_list.insert(2, 55)  #=> [5, 6, 55, 7, 12, 10]
print(my_list)       

#------------------------------------------------------------------------------------------------
# Removes the element from the end by default
my_list=[5, 6 ,7 ,12 , 10]
poped_value = my_list.pop()  #=> [5, 6, 7, 12]
print(my_list)
print(f"poped_value: {poped_value}")   #=> poped_value: 10

#Can also pop value from specific index but this operation is recommanded to remove value from the end
poped_value = my_list.pop(2)  #=> [5, 6, 12]
print(my_list)                   
print(f"poped_value: {poped_value}")  #=> poped_value: 7

#------------------------------------------------------------------------------------------------
# Removes given value from the list
my_list=[5, 6 ,7 ,12 , 10]
my_list.remove(12)  #=> [5, 6, 7, 10]
print(my_list)

removed_value = my_list.remove(5)  #=> [6, 7 ,10]
print(my_list)                   

#------------------------------------------------------------------------------------------------
# Reverse list
my_list=[5, 6 ,7 ,12 , 10]
my_list.reverse()    # => [10, 12, 7, 6, 5]
print(my_list)

#------------------------------------------------------------------------------------------------
# Length of list
my_list=[5, 6 ,7 ,12 , 10]
print(len(my_list)) #=> 5

#------------------------------------------------------------------------------------------------
# Get index of the element
my_list=[5, 6 ,7 ,12 , 10]
print(my_list.index(7)) #=> 2

#------------------------------------------------------------------------------------------------
# Count how many times given element is there in the list
my_list=[5, 6 ,7 ,12 , 10, 10, 12, 12, 7]
print(my_list.count(12)) #=> 3

#------------------------------------------------------------------------------------------------
# Sort the list  => do not return anything directly sort the list
my_list=[5, 6 ,7 ,12 , 10, 10, 12, 12, 7]
my_list.sort()           # Sort in ascending Order # [5, 6, 7, 7, 10, 10, 12, 12, 12]
print(my_list)

my_list=[5, 6 ,7 ,12 , 10, 10, 12, 12, 7]
my_list.sort(reverse=True)           # Sort in decending Order # [12, 12, 12, 10, 10, 7, 7, 6, 5]
print(my_list)





