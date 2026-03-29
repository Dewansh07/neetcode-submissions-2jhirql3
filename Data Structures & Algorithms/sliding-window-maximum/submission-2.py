class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        dq = deque()

        for i in range(len(nums)):

            # remove the element that went out of window
            if dq and dq[0] == i-k:
                dq.popleft()

            # remove the smaller element
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)

            #append to arr when window is formed
            if i>=k-1:
                arr.append(nums[dq[0]])
        return arr