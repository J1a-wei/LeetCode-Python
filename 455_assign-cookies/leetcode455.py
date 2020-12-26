from typing import List


class Solution:
    def findContentChildren(self,g: List[int],s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        children = 0
        cookies = 0
        while children < len(g) and cookies < len(s):
            if g[children] <= s[cookies]:
                children +=1
            cookies +=1
        return children