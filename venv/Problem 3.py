# Good morning!
# This is your coding interview problem for today.
# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    s = ''
    if root.left:
        s = s + serialize(root.left)
    else:
        s = s + '#,'
    if root.right:
        s = s + serialize(root.right)
    else:
        s = s + '#,'
    s = root.val + ',' + s
    return s

def deserialize(s):
    def des_help():
        node = next(nodes)
        if node == '#':
            return None
        node = Node(node)
        node.left = des_help()
        node.right = des_help()
        return node
    nodes = iter(s.split(','))
    return des_help()

# The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).right.val == 'right'

print(serialize(node))
print(serialize(deserialize(serialize(node))))

# Lot of extra time trying to make my old solution work, but ultimately the failing was my shoehorning of
# Java programming principles onto Python - without specific object references, my approach to the
# scope problem was not feasible. Separating the recursive function and node setting from the iteration and
# into different scope was key - I was not aware of Python iterators until I looked into this issue.

