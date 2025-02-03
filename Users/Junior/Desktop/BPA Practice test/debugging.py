def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    #in the original it was print(factorial[5]) the brackets wouldnt work with this so it needed parentheses instead.
print(factorial(5))