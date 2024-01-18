
############Add Item in set###################
#1. Using add method
my_set = {1,2,3}
my_set.add(5)    #=> {1, 2, 3, 5}
print(f"After adding single item in set : {my_set}")

#2. using update method
# Add set/any iterable(list/tuple) in set using update method
set1 = {'java' , 'python'}
set2 = {'shell_scipt' , 'c language'}
set1.update(set2)
print(f"After merging set2 in set1 : {set1}")          #=> { 'java' , 'python' , ''shell_script' , 'c language' }
list1 = ["maths", "physics" , "physics" , "science" ]
set1.update(list1)
print(f"After merging list1 in previous set1 : {set1}")         #=> { 'java' , 'python' , ''shell_script' , 'c language', "maths" , "physics" , "science" }
#####################################

print("\n")


###Remove items from the setusing remove and discard method#########
set1 = {'java' , 'python'}
set1.remove('java')         #=> {'python'}
print(f"after remove: {set1}")
set1 = {'java' , 'python'}
set1.discard('java')        #=> {'python'}
print(f"after discard : {set1}")

## clear set
set1.clear()   # set() => it will provide empty set as now its clear
# print(set1)

## Remove the set
del set1
# print(set1) => will give error as set has been deleted
###################################################################

print("\n")

# # Union, Intersection, Difference 
# #This operation will provide new set so the sets we are using in operation will be unchanged

######### 1. Union of set: #############
set1 = {1 , 2 , 3}
set2 = {4 , 5 , 6}
set3 = set1.union(set2) #=> {1, 2, 3, 4, 5, 6}
print(f"union of set1: {set1} and set2: {set2} : {set3}")
#OR
set4 = set1 | set2      #=> {1, 2, 3, 4, 5, 6}
print(f"union of set1: {set1} and set2: {set2} using | synmbol : {set4}")

# update() method to union set1 and set2 
set1.update(set2)
print(f"after update set1 : {set1}")   #=> {1, 2, 3, 4, 5, 6}  # NOTE: it will update the value of set1 as per the operation
###########################################

print("\n")

########## 2. Intersection of set: ##########
set1 = { 1, 2, 3 }
set2 = { 2, 3, 4 }
set3 = set1.intersection(set2)  #=> { 2, 3 }
print(f"intersection of set1: {set1} and set2: {set2} : {set3}")
#OR
set4 = set1 & set2              #=> { 2, 3 }
print(f"intersection of set1:{set1} and set2:{set2} using & symbol : {set4}")

# intersection_update()
set1.intersection_update(set2)   #=> { 2, 3 }   it will update the value of set1 as per the operation
print(f"after intersection_update set1 : {set1}")                  
#############################################

print("\n")

########## 3. difference in set:  ###########
set1 = { 1, 2, 3, 5 }
set2 = { 2, 3, 4 }
set3 = set1.difference(set2)  #=> { 1, 5 }
print(f"difference of set1: {set1} and set2: {set2} : {set3}")
#OR
set4 = set1 - set2            #=> { 1, 5 }
print(f"difference of set1: {set1} and set2: {set2} using - symbol : {set4}")
set5 = set2 - set1            #=> { 4 }
print(f"difference of set2: {set2} and set2: {set1} using - symbol : {set5}")

# difference_update()
set1.difference_update(set2)   
print(f"after difference_update set1 : {set1}")                  #=> {1,5}   it will update the value of set1 as per the operation
##############################################

print("\n")

######## 4. Symmetric Difference  ############
# The symmetric difference between two sets is the set of all the elements that are either in the first set or the second set but not in both.
set1 = { 1, 2, 3, 5 }
set2 = { 2, 3, 4 }
set3 = set1.symmetric_difference(set2)  #=> { 1, 4, 5 }
print(f"symmetric_difference of set1: {set1} and set2: {set2} : {set3}")
# OR
set4 = set1 ^ set2              #=> { 1, 4, 5 }
print(f"symmetric_difference of set1: {set1} and set2: {set2} using ^ symbol : {set4}")

# symmetric_difference_update
set1.symmetric_difference_update(set2)
print(f"after difference_update set1 : {set1}")       #=> { 1, 4, 5 }   it will update the value of set1 as per the operation
#################################################


print("\n\n")

########## Conditions ###########
set1 = {1,2,3,4,5,6}
set2 = {1,2,3}
set3 = {4,5,6}

# isdisjoint()		Returns whether two sets have a intersection or not
print(f"is set1: {set1} and set2: {set2} disjoint ? = {set1.isdisjoint(set2)}")
print(f"is set2: {set2} and set3: {set3} disjoint ? = {set2.isdisjoint(set3)}")


# issubset()		Returns whether another set contains this set or not
print(f"is set2: {set2} subset of set1: {set1} ? = {set2.issubset(set1)}")
print(f"is set2: {set2} subset of set3: {set3} ? = {set2.issubset(set3)}")

# issuperset()		Returns whether this set contains another set or not
print(f"is set1: {set1} superset of set2: {set2} ? = {set1.issuperset(set2)}")
print(f"is set2: {set2} superset of set3: {set3} ? = {set2.issuperset(set3)}")
################################

print("\n")
### remove duplicate from list using set ###

list1 = [1,2,2,3,4,5,5,2]
list1_without_duplicate = list(set(list1)) #=> convert to set will remove duplicate and then convert to list
                                           # here order might change as set do not manage order of element
print(list1_without_duplicate)             



######## TASK ##########
# Create two list and apply all the methods which we have learn
# Create list of string which have duplicates and remove dumplicates using set.