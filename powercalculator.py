base = float(input("Enter the base number: "))
n = int(input("Enter how many powers you want to calculate: "))

print(f"\nPowers of {base} up to {n}:\n")

for i in range(1, n + 1):
    print(f"{base}^{i} = {base ** i}")