"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        if root is None :
            return []
        result =[]
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[:])
        return result[::-1]

