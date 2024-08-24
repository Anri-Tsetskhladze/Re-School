#BMI Calculator 
import colorama
from colorama import init, Fore, Back, Style

init()  # Initialize colorama for colored text output

print(Back.GREEN + "Welcome to Anri Tsetskhladze's Children Age software.")
print(Back.CYAN)

try:
    age = float(input("What's your age ?: "))
    

    if age <= 0:
        raise ValueError("ERROR Are You Alive ")

except ValueError as e:
    print(Back.RED + f"Error: Invalid input: {e}")
    exit()

if age < 2 :
    print(Back.RED + " You Are a Baby")
elif age > 2:
    print(Back.GREEN + "You Are a Children")
elif age >16:
    print(Back.YELLOW + "You Are a Young Adult")
elif age > 30:
    print(Back.ORANGE + "You Are a Middle-Aged Adult")
elif age > 45:
    print(Back.RED + "You Are a Adult")


print("")
print(Style.RESET_ALL)

input("Press Enter to exit...")