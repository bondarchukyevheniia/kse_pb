import random
from data import words
def generate():
    secret_word = random.choice(words)
    wl = len(secret_word)
    return secret_word, wl
