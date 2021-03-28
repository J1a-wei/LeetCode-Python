"""
# Definition for a Node.

"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None :
            return []
        result = []
        stack = [root]
        while stack:
            length = len(stack)
            subResult = []
            for i in range(length):
                node = stack.pop(0)
                subResult.append(node.val)
                stack.extend([n for n in node.children if n ])
            result.append(subResult)
        return result

y = 55