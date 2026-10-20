class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def can_eat(speed):
            hour = 0

            for pile in piles:
                hour+= (pile+speed-1)//speed

            return hour<=h
        
        while l<r:
            mid = (l+r)//2

            if can_eat(mid):
                r = mid
            else:
                l = mid+1
        return l