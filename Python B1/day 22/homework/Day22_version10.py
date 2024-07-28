#https://www.codewars.com/kata/6512b3775bf8500baea77663/train/python

def gimme_the_letters(sp):
    start, end = sp.split('-')
    
    return ''.join(chr(i) for i in range(ord(start), ord(end)+1))

print(gimme_the_letters("a-z"))  
print(gimme_the_letters("h-o"))  
print(gimme_the_letters("Q-Z")) 
print(gimme_the_letters("J-J")) 
