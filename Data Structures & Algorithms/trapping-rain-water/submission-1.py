class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = height[left]
        max_right = height[right]
        total = 0

        while left<right:
            if height[left]<height[right]:
                if max_left<height[left]:
                    max_left = height[left]
                else:
                    total+= (max_left-height[left])
                left+=1
            else:
                if max_right<height[right]:
                    max_right = height[right]
                else:
                    total+=(max_right-height[right])
                right-=1
        return total