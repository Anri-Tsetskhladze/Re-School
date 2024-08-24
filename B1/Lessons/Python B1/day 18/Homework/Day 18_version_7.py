def demo_remove_duplicates():
    numbers = input("Enter numbers separated by commas: ")
    num_list = [int(num) for num in numbers.split(',')]
    unique_list = list(set(num_list))
    print(f"List without duplicates: {unique_list}")

demo_remove_duplicates()
