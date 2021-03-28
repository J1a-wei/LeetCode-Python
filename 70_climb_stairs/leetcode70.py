# dp

def climbStairs1(self, n: int) -> int:
    if n == 1 or n == 2:
        return n
    arr = [0 for x in range(0, n + 1)]
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]


# dp 状态压缩
def climbStairs2(self,n: int) -> int :
    if n == 1 or n == 2 :
        return n
    a,b,tmp = 1,2,0
    for i in range(3,n+1):
        tmp = a + b
        a = b
        b = tmp
    return  tmp

# dfs cached 剪枝

def climbStairs(self,n: int)-> int :
    cached = {1:1,2:2}
    def dfs(n,cached):
        if n not in cached: cached[n] = dfs(n - 1,cached) + dfs(n -2 ,cached)
        return cached[n]
    return dfs(n,cached)