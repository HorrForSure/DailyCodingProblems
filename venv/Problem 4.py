# This is your coding interview problem for today.
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def missing_positive_integer(x):
    s = set(x)
    i = 1
    while i in s:
        i += 1
    return i

input = [3, 4, -1, 1]
input2 = [1, 2, 0]
print(missing_positive_integer(input))
print(missing_positive_integer(input2))

# Essentially ended up using the set implementation from the given solution, as I was not aware of the massive
# efficieny gap for checking existence in a set versus sorting and traversing the original list (since the
# difference in time complexity between the two (O(n) vs O(nlog(n))) is what allows a set to be used for this problem).


