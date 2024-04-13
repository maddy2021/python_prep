# 407
# sum of cube of each digit should be same as number
# example:
# 4**3 + 0 **3 + 7**3 = 64+ 0 + 343 = 407

number = 407

summation = 0

while number>0:
    digit = number%10
    summation = summation + (digit**3)
    number = number//10

print(f"summation: {summation}")

if summation == number:
    print("number is armstrong")
else:
    print("number is not armstrong")