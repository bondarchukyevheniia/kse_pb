import random
from data import words
def resultt():
    result=[]
    i=0
    tries = 6
    wl = len(secret_word)
    secret_word = random.choice(words)
    guess = input(f"Attempt {7 - tries}/6 Enter guess").lower()
    while i<wl:
        letter = guess[i]
        if letter==secret_word[i]:
            result.append('correct')
        elif letter in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i+=1
    return result