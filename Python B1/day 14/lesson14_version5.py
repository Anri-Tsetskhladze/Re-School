
names_array = ["John", "Jane", "Doe"]


age = int(input("Enter your age: "))


if age > 18:
   
    user_name = input("Enter your name: ")

   
    if user_name:
      
        names_array.append(user_name)


print("Final Array:", names_array)
