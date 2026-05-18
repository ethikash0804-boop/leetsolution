class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        one = 2
        two = 1

        for i in range(3, n + 1):
            temp = one + two
            two = one
            one = temp

        return one