import random

words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
secret_word = random.choice(words)

tries = 6
wl = len(secret_word)


print("Welcome to Wordle!")
print("Guess the",wl,"-letter word. You have", tries, "tries.")

while tries!=0:
    guess = input(f"Attempt {7 - tries}/6 Enter guess").lower()
    if len(guess)!=wl:
        print("Wrong length. Expected length:", wl)
        continue
    elif guess==secret_word:
        print("You win!!!")
        break

    result=[]
    i=0
    while i<wl:
        letter = guess[i]
        if letter==secret_word[i]:
            result.append('correct')
        elif letter in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i+=1

    display=[]
    j=0
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

    print("Result:", ' '.join(display))
    tries-=1
else:
    print("You lose! The word was:", secret_word)