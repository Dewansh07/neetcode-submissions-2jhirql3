class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = defaultdict(int)
        st = defaultdict(int)

        for i in s:
            sc[i] += 1
        for j in t:
            st[j]+=1

        return sc == st