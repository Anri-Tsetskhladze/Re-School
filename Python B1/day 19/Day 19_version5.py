#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

#The output should be two capital letters with a dot separating them.

#It should look like this:

#Sam Harris => S.H

#patrick feeney => P.F

def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"

print(abbrev_name("Sam Harris"))       
print(abbrev_name("patrick feeney"))   

