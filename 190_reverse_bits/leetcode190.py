class Solution:
    def reverseBits(self, n: int) -> int:
        # solution int -> str -> reverse -> int
        # solution2 move one by one
        res = 0
        for i in range(32):
            res = res << 1
            res |= n&1
            n = n >> 1
        return res
