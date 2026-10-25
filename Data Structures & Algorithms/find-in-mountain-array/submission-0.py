class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        def find_targets(left,right,target,upside):
            while left<=right:
                mid = (left+right)//2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    return mid

                if upside:
                    if mid_val >target:
                        right = mid-1
                    else:
                        left = mid+1
                else:
                    if mid_val>target:
                        left = mid+1
                    else:
                        right = mid-1
            return -1

        def find_peak():
            nonlocal length
            left = 0
            right = length-1
            while left<right:
                mid = (left+right)//2
                if mountainArr.get(mid)<mountainArr.get(mid+1):
                    left = mid+1
                else:
                    right = mid
            return left

        peak_idx = find_peak()

        result = find_targets(0,peak_idx,target,True)

        if result !=-1:
            return result
        return find_targets(peak_idx+1,length-1,target,False)