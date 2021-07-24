# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def summable(k, n):
    m = [0 for _ in range(len(n))]
    for i in range(len(n)):
        for j in range(i):
            if m[j] == n[i]:
                print(m)
                return True
        m[i] = k - n[i]
    return False

# Worst case should be O(n^2), if the entire first array is traversed, and the amount of array m
# being traversed is n[i], where i = len(n - 1).