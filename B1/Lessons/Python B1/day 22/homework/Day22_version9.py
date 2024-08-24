#https://www.codewars.com/kata/65dd5b414ccda60a4be32c2a/train/python

def gaslighting(shirt_word: str, your_word: str, friends_letters: list) -> bool:
    for s_letter, y_letter in zip(shirt_word, your_word):
        if s_letter != y_letter and s_letter in friends_letters:
            return True
    return False

print(gaslighting("snack", "snake", ["c"])) 
print(gaslighting("snack", "snack", ["s", "n", "a", "c", "k"]))
print(gaslighting("snake", "snack", ["c"]))
print(gaslighting("smile", "smirk", ["s", "m", "i"])) 
