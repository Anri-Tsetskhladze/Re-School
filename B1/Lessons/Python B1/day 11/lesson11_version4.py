pincode = 5793
balance = 75543
depozite = 634

while True:
    user_pincode = int(input("Enter Your Pincode: "))
    if user_pincode == pincode:
        print("Your Balance is: " + str(balance) + ", Your Deposit is: " + str(depozite))
        break  
        print("Incorrect Pincode. Try Again")