# DFS 剪枝
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(leftCount, rightCount, str):
            if leftCount == n and rightCount == n:
                result.append(str)

            if leftCount < n:
                dfs(leftCount + 1, rightCount, str + '(')

            if leftCount > rightCount:
                dfs(leftCount, rightCount + 1, str + ')')

        dfs(0, 0, "")
        return result

