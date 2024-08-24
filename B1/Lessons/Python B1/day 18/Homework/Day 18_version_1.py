def demo_filter_multiples_of_4():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    num_list = list(range(start, end + 1))
    filtered_list = [num for num in num_list if num % 4 == 0]
    print(f"Multiples of 4 between {start} and {end}: {filtered_list}")

demo_filter_multiples_of_4()
