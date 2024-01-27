#We have a list with random numbers
#Task:Now create 2 seperate lists, 1 will contain odd and 2 will contain even numbers

number_list=[1,2,7,17,54,87,29,9,45,93,43,5,7,6]
odd_list=[]
even_list=[]

for i in number_list:
    if i%2!=0:
        odd_list.append(i)
    else:
        even_list.append(i)

print(odd_list)
print(even_list)    

#Remove duplicates from lists
my_list=[2,3,3,5,6,6,90,90]
new_list=[]

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)      

#armstrong number
#153 = 1+125+27 = 153

num= int(input("Enter the number:"))
num_input = num
sum_num=0
while num>0:
    reminder=num%10
    sum_num = sum_num + (reminder**3)
    num = num // 10

if num_input==sum_num:
    print("It is armstrong")
else:
    print("Not an armstrong")

#Pallindrome number
#121     

num= int(input("Enter the number:"))
num_input = num
rev=0
while num>0:
    reminder=num%10
    rev = (rev * 10 ) + reminder
    num = num // 10

if num_input==rev:
    print("It is pallindrome")
else:
    print("Not pallindrome")
    
#Find max number from the list
    
my_list=[1,67,90,4,5,7,78]
max_num = 0
min_num = 1000

for i in my_list:
    if i > max_num:
        max_num=i

for i in my_list:
    if i < min_num:
        min_num = i

print(min_num)                
print(max_num)        
