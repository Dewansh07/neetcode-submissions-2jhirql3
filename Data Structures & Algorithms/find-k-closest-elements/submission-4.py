class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # minheap = []

        # for num in arr:
        #     heapq.heappush(minheap, (abs(num-x),num))

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(minheap)[1])
        # res.sort()

        # return res

        # left = 0
        # right = len(arr)-k

        # while left<right:
        #     mid = (left+right)//2
        #     if x-arr[mid] > arr[mid+k]-x:
        #         left = mid+1
        #     else:
        #         right = mid
        # return arr[left:left+k]

        left = 0
        right = len(arr)-1

        while right-left+1>k:
            if abs(arr[left]-x)>abs(arr[right]-x):
                left+=1
            else:
                right-=1

        return arr[left:left+k]