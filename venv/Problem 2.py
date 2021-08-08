# Good morning!
# This is your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def other_product(x):
    product = x[0]
    y = [0 for _ in range(len(x))]
    for i in range(1, len(x)):
        product = product * x[i]
    for i in range(len(x)):
        y[i] = product / x[i]
    return y

# Follow-up: what if you can't use division?

def op_nodiv(x):
    prefix_products = []
    for num in x:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    suffix_products = []
    for num in reversed(x):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    products = []
    for i in range(len(x)):
        if i == 0:
            products.append(suffix_products[i + 1])
        elif i == len(x) - 1:
            products.append(prefix_products[i - 1])
        else:
            products.append(prefix_products[i - 1] * suffix_products[i + 1])
    return products

# Intuition about using a prefix and suffix list of products was correct, but my implentation was very shoddy when
# I first started writing it. Refined to match given solution, but still getting readjusted to syntax.