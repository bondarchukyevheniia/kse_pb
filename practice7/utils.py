def is_prime(n):
    for i in range(1,n//2+1):
        if n%i==0:
            g = False
        else:
            g = True
    return g