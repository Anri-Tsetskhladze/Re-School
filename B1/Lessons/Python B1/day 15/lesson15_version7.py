num1 = float(input("ჩაწერე პირველი რიცხვი: "))
num2 = float(input("ჩაწერე მეორე რიცხვი: "))


operator = input("აირჩიე ოპერატორები (+, -, *, /, ^): ")


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("შეცდომა ნულზე გაყოფა არ შეიძლება.")
        result = None
    else:
        result = num1 / num2
elif operator == "^":
    result = num1 ** num2
else:
    print("შეცდომა.")
    result = None

if result is not None:
    print(f"პასუხი {result}.")