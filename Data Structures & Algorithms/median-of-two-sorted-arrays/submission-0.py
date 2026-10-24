class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        if len(a)>len(b):
            a,b = b,a

        total = len(a)+len(b)
        half = total//2

        l,r = 0,len(a)
        while l<=r:
            mid = (l+r)//2
            i = mid
            j = half-i

            lefta = a[i-1] if i>0 else float('-inf')
            righta = a[i] if i<len(a) else float('inf')

            leftb = b[j-1] if j>0 else float('-inf')
            rightb = b[j] if j<len(b) else float('inf')

            if lefta<=rightb and leftb<=righta:
                if total%2:
                    return float(min(righta,rightb))
                return (max(lefta,leftb) + min(righta,rightb))/2

            elif lefta>rightb:
                r = mid-1
            else:
                l = mid+1