# Good morning!
# This is your coding interview problem for today.
# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.
def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

# Had to read up on lambda expressions to understand how to slot in for the anonymous function f. I recognized the
# function names from my brief time using Scheme, but the syntax threw me off here, especially in the 'cons' block.