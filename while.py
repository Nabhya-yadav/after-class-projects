num = input("Enter a number: ")

clean_num = ""
i = 0

while i < len(num):
    if num[i].isdigit():
        clean_num += num[i]
    i += 1

print("Number of digits:", len(clean_num))
