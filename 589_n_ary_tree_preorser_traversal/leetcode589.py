from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class DfsSolution(object):
    def preorder(self,root) -> List[int]:
        def dfs(node,result):
            if node is None:
                return
            result.append(node.val)
            for sub in node.children:
                dfs(sub,result)

        result = []
        dfs(root,result)

        return result




class IterateSolution(object):
    def preorder(self,root) -> List[int]:
        stack = [root]
        result = []
        if stack is None:
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
            # for sub in node.children[::-1]:
            #     stack.append(sub)
        return result
