class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def totaldays(capacity):
            days = running_sum = 0
            for weight in weights:
                if running_sum+weight >capacity:
                    days+=1
                    running_sum = weight
                else:
                    running_sum+=weight
            return days+1 if running_sum>0 else days

        while l<r:
            mid = l + (r-l)//2

            if totaldays(mid)<= days:
                r = mid
            else:
                l = mid+1
        return l