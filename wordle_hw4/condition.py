def condition(secret_word):
    tries = 6
    wl = len(secret_word)
    while tries!=0:
        guess = input(f"Attempt {7 - tries}/6 Enter guess").lower()
        if len(guess)!=wl:
            print("Wrong length. Expected length:", wl)
            continue
        if guess==secret_word:
            print("You win!!!")
            break
        else:
            print("You lose! The word was:", secret_word)
    return()