def demo_transform_numbers():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    transformed_list = [i**2 if i % 2 == 0 else i**0.5 for i in range(start, end + 1)]
    print(f"Transformed numbers: {transformed_list}")

demo_transform_numbers()
