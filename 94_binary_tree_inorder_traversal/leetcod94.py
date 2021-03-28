# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class DFSSolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.dfs(root,result)
        return result
    def dfs(self,node,result):
        if node is None:
            return
        self.dfs(node.left, result)
        result.append(node.val)
        self.dfs(node.right, result)