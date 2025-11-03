n = 7 # decimal number

result = "" # binary result

while n > 0:

    result = str(n & 1) + result

n >>= 1

print(result)