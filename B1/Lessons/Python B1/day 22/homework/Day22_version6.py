#https://www.codewars.com/kata/5a1c28f9c9fc0ef2e900013b/train/python
def pyramid(n):
    pyramid_str = ""
    
    for i in range(n):
        leading_spaces = ' ' * (n - i - 1)
        middle_spaces = ' ' * (2 * i)
        if i == 0:
            pyramid_str += leading_spaces + "/\\" + "\n"
        else:
            pyramid_str += leading_spaces + "/" + middle_spaces + "\\" + "\n"
    
    pyramid_str += "/" + "_" * (2 * n - 2) + "\\" + "\n"
    
    return pyramid_str

