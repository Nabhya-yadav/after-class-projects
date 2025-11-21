num = int(input("Enter a number: "))

count = 0
temp = abs(num)   # to handle negative numbers

while temp != 0:
    temp = temp // 10
    count += 1

# special case: if number is 0
if num == 0:
    count = 1

print("Number of digits:", count)
