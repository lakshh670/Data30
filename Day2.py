
num = int(input("Enter a number: "))

print("\nMultiplication Table using for loop:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\nMultiplication Table using while loop:")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
