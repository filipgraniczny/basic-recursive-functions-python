# This is a basic implementation of the recursive fibonacci method in Python3

def fib(a):
    if a <= 1:
        return a
    return fib(a-2) + fib(a-1)
