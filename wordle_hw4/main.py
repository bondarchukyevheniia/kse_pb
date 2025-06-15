import random
from data import words
secret_word = random.choice(words)
tries = 6
wl = len(secret_word)
print("Welcome to Wordle!")
print("Guess the",wl,"-letter word. You have", tries, "tries.")
from generate import generate
def generate():
    secret_word = random.choice(words)
    wl = len(secret_word)
    return secret_word, wl
from condition import condition
from resultt import resultt