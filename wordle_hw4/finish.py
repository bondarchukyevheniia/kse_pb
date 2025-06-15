import random
from resultt import result
wl = len(secret_word)
secret_word = random.choice(words)
tries = 6
guess = input(f"Attempt {7 - tries}/6 Enter guess").lower()
display=[]
j=0
def finish():
    while j<wl:
        s = guess[j]
        res = result[j]
        if res=='correct':
            display.append("["+s.upper()+"]")
        elif res=='present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1
    return