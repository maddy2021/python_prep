number = 343
#number = 324

rev_number=0
while number>0:
    mod = number%10
    rev_number = rev_number+mod
    number = number//10

print(f"reverse number: {rev_number}")

if number == rev_number:
    print("Its palindrome")
else:
    print("It's not palindrome")

