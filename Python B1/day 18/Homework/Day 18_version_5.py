def demo_calculate_mean():
    numbers = input("Enter numbers separated by commas: ")
    number_list = [float(num) for num in numbers.split(',')]
    mean = sum(number_list) / len(number_list)
    print(f"Arithmetic mean: {mean}")

demo_calculate_mean()
