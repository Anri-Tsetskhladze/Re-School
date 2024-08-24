user_number = int(input("Enter a number: "))

if user_number % 3 == 0 and user_number % 5 == 0:
    print("FizzBuzz")
elif user_number % 3 == 0:
    print("Fizz")
elif user_number % 5 == 0:
    print("Buzz")
else:
    print(user_number)