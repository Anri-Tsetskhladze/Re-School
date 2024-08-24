
num = int(input("ჩაწერე პირველი რიცხვი: "))

if num % 2 == 0:
    print(f"{num} არის ლუწი.")
else:
    print(f"{num} არ არის ლუწი.")
    next_even = num + (2 - num % 2)
    print(f"შემდეგი ციფრი არის  {next_even}.")

