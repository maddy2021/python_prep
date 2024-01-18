# Duplicate keys are not allowed and it wont give error but assign the last duplicate key value
# example:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 1966
# }

# Result:
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1966}


##############################################################################################################
my_dict = {
    "name" : "xyz",
    "phn_num" : 92472386467,
    "email_id" : "xyzgmail.com",
    "hobbies" : ["sports", "music", "movies"]
}

# Print hobbies and email_id from dictionary
print(my_dict["hobbies"])        #['sports', 'music', 'movies']
print(my_dict["email_id"])       #xyzgmail.com
# print(my_dict["unknown"])   #=> Error
# Traceback (most recent call last):
#   File "E:\python_practice\python_prep\module_2\dict.py", line 11, in <module>
#     print(my_dict["unknown"])   #=> Error
# KeyError: 'unknown'


# Using get method it will not give error is key was not present in list
# Use this in place of getting by key
print(my_dict.get("hobbies"))    #['sports', 'music', 'movies']
print(my_dict.get("email_id"))   #xyzgmail.com
print(my_dict.get("unknown"))    # None  => it will not give error

# Print all the keys from dictionary using keys() method
print(my_dict.keys())           # dict_keys(['name', 'phn_num', 'email_id', 'hobbies'])

# Print All values from the dictionary using values() method
print(my_dict.values())         # dict_values(['xyz', 92472386467, 'xyzgmail.com', ['sports', 'music', 'movies']])

#print key value pair using items() method
print(my_dict.items())          #dict_items([('name', 'xyz'), ('phn_num', 92472386467), ('email_id', 'xyzgmail.com'), ('hobbies', ['sports', 'music', 'movies'])])


# Add/update new key value to dict 
# If key is already present it will update its value and if key is not present it will add key value pair to the dictionary
# suppose add Country
my_dict["country"] = "IN"
print(my_dict)   # {'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'xyzgmail.com', 'hobbies': ['sports', 'music', 'movies'], 'country': 'IN'}

my_dict.update({"state":"GJ"})  #{'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'pqr@gmail.com', 'hobbies': ['sports', 'music', 'movies'], 'country': 'IN', 'state': 'GJ'}
print(my_dict)

#update email_id
my_dict["email_id"] = "pqr@gmail.com"
print(my_dict)   # {'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'pqr@gmail.com', 'hobbies': ['sports', 'music', 'movies'], 'country': 'IN'}

my_dict.update({"email_id":"xyzpqr@gmail.com"})  #{'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'xyzpqr@gmail.com', 'hobbies': ['sports', 'music', 'movies'], 'country': 'IN', 'state': 'GJ'}
print(my_dict)


# lenth of dictionary
print(len(my_dict))


# Remove key value from the dictionary
# Using pop method
poped_item = my_dict.pop("state")   # {'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'xyzpqr@gmail.com', 'hobbies': ['sports', 'music', 'movies'], 'country': 'IN'}
print(my_dict)
print(f"poped item is: {poped_item}")  # poped item is: GJ

# Using popitem() : Ordered dict remove last element from dictionary
poped_item = my_dict.popitem()   # {'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'xyzpqr@gmail.com', 'hobbies': ['sports', 'music', 'movies']}
print(my_dict)
print(f"poped item is: {poped_item}")  # poped item is: ('country', 'IN')

# using del keyword
del my_dict["hobbies"]  # {'name': 'xyz', 'phn_num': 92472386467, 'email_id': 'xyzpqr@gmail.com'}
print(my_dict)


# clear dictionary
my_dict.clear()
print(my_dict)

# Delete dictionary
del my_dict
#print(my_dict)  # it will give error as dict already deleted
# Traceback (most recent call last):
#   File "E:\python_practice\python_prep\module_2\dict.py", line 65, in <module>
#     print(my_dict)
# NameError: name 'my_dict' is not defined



# Nested Dict, dictionary inside dictionary 
my_profile = {
    "name": "xyz",
    "phn_num" : 92472386467,
    "email_id" : "xyzgmail.com",
    "hobbies" : ["sports", "music", "movies"],
    "Address" : {
        "country" : "IN",
        "state"  : "GJ",
        "city"   : "AP",
        ("lat","long") : (10.55,10.66),
        "postal_code": 390056,
        "sub_details": {
            "street" : "pqr",
            "house_no": "b-7",
            "landmark": "lop school"
        }
    }
}

#Assignment

#Task-1
########
# print lat,long
# print address dictionary
# print street
# print long

#Task-2
# print items for address
# print keys of sub_details
# print values of address

#Task-3
# change country
# change postalcode
# try to change long => do analysis what are you getting
# change house_no
# add "writing" in hobbies


#Task-4
# remove landmrk
# remove sub_details dictionary
# remove "movies" from hobbies


