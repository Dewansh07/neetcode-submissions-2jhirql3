class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def can_eat(speed):
            hour = 0
            for pile in piles:
                hour+= (speed+pile-1)//speed
            return hour<=h


        while left<right:
            mid = left + (right-left)//2

            if can_eat(mid):
                right = mid
            else:
                left = mid+1
        return left