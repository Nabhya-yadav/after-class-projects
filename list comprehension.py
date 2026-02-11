number = [1,2,3,4,5]

even = [x for x in number if x % 2 == 0]
odd=[x for x in number if x % 2!=0]

print("even number from the list : " , even)
print("odd number from the list : " , odd)