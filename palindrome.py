# This is a basic implementation of the recursive palindrome method in Python3

def palindrome(a):
    if len(a) < 2:
        return True
    return (a[0] == a[len(a)-1]) and palindrome(a[1:len(a)-2])

