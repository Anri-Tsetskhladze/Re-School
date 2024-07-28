#1.Convert a String to a Number!
def string_to_number(s):
     return int(s)

#2.Convert a String to a Number!
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    a / b
def mod(a, b):
    return a % b 

def exponent(a, b):
    return a ** b

def subt(a, b):
    return a - b


# 3
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# 4
def combine_names(first, last):
    return first + " " + last

# 5 All Star Code Challenge 

def strCount(string, letter):
    return string.count(letter)