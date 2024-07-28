def filter_even_index_letters(full_name):
    names = full_name.split()
    last_name = names[-1]  
    
    even_index_letters = []
    
    for i in range(len(last_name)):
        if i % 2 == 0:  
            even_index_letters.append(last_name[i])
    
    filtered_last_name = ''.join(even_index_letters)
    
    return filtered_last_name


full_name = "Mr NoName"
print(filter_even_index_letters(full_name))
