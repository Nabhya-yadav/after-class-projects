
ch = input("Enter a character: ")


if len(ch) == 1:
    
    if ch.isalpha():
        print(f"{ch} is an alphabet.")
    else:
        print(f"{ch} is not an alphabet.")
else:
    print("Please enter only one character.")