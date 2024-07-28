
incorrect_count = 0

correct_password = "Goa best"

while True:
    user_password = input("Enter your password: ")
    incorrect_count += 1
    
    if user_password == correct_password:
        print("Correct password!")
        break


print(f"Number of incorrect passwords: {incorrect_count}")