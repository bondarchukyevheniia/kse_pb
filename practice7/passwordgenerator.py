import random
import string
def generate_password(length, allow_symbols):
    if allow_symbols==True:
        password1 = string.ascii_letters
        password2 = string.digits
        password4 = string.punctuation
        password3 =random.choices(password1+password2+password4, k=length)
    else:
        password5 = string.ascii_letters+string.digits
    password6 =  random.choices(password5, k=length)
    return password6
