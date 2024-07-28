num = int(input("Enter a number: "))

even_numbers = []

for i in range(num + 1):
    if i % 2 == 0:
        even_numbers.append(i)

print("The even numbers in the range from 0 to Your 's number are:")
print(even_numbers)