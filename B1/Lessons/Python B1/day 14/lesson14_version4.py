first_number = int(input("Enter the first number : "))

second_number = int(input("Enter the second number : "))

start_number = min(first_number, second_number)
end_number = max(first_number, second_number)


print(f"Multiples of five between {start_number} and {end_number}:")

for num in range(start_number, end_number + 1):
    if num % 5 == 0:
        print(num)
