class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left,right = max(weights), sum(weights)

        def totaldays(capacity):
            day = running_sum = 0

            for weight in weights:
                if running_sum + weight > capacity:
                    day+=1
                    running_sum = weight
                else:
                    running_sum+=weight
            day+=1 if running_sum >0 else day
            return day

        while left<right:
            mid= left+(right-left)//2

            if totaldays(mid)<=days:
                right = mid
            else:
                left = mid+1
        return left

