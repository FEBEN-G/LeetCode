class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        prevprev = 1
        prev = 2
        curIdx = 3
        while curIdx <= n:
            current = prev + prevprev
            prevprev = prev
            prev = current
            curIdx += 1
        return prev