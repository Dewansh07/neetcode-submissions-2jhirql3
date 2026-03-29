class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        max_left = height[left]
        max_right = height[right]
        count = 0

        while left<right:
            if height[left]<height[right]:
                if height[left]>max_left:
                    max_left = height[left]
                else:
                    count+= (max_left - height[left])
                left+=1
            else:
                if height[right]>max_right:
                    max_right = height[right]
                else:
                    count+=(max_right- height[right])
                right-=1
        return count
