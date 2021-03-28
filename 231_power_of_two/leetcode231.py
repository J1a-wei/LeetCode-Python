class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2的幂代表的意义是什么： 在二进制数的形态下，有且只有一个1
        return n != 0 and (n &(n - 1)) == 0
