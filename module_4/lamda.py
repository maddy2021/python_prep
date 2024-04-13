#  lambda fun para : expression
# multi = lambda a,b : a * b

# # def multi(a,b):
# #     return a*b

# print(multi(20,11))

# take a list and return sum of list

from functools import reduce

def summation(list1):
    my_sum =0 
    for item in list1:
        my_sum = my_sum+item
    return my_sum


list1=[10,20,30]
sum_lamda = lambda a,b : a*b
summation = reduce(sum_lamda ,list1)
print(summation)


# Map : same operation of each element of item and return the list
# new_list = [50,100,150]
multi_5 = list(map(lambda a : a*5 ,list1))
print(multi_5)
# [10,20,30,40]

list2 = [10,20,30]
# list2= ['10','20','30']
print(list(map(str,list2)))

# Filter : filter out data from the list 
# new_list = [50,100,150]
list1 = [5,10,12,11,66,77,100]
even_number = list(filter(lambda a: a%2!=0, list1))
print(even_number)

list1 = ["hello","world","sky","earth","baloo","jena"]

def string_match(your_string):
    if("oo" in your_string):
        return True
    if("je" in your_string):
        return True
    return False

list2 = list(filter(string_match, list1))
print(list2)