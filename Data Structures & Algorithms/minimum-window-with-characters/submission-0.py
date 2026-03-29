class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        scount = Counter(s)
        l = 0
        start = 0
        min_len = float("inf")
        win = defaultdict(int)


        for i in tcount:
            if tcount[i]>scount[i]:
                return ""
        
        def contains_all(w,t):
            for i in t:
                if w[i]<t[i]:
                    return False
            return True

        for r in range(len(s)):
            win[s[r]]+=1

            while contains_all(win,tcount):
                if r-l+1<min_len:
                    min_len=r-l+1
                    start = l
                win[s[l]]-=1
                l+=1
        
        return "" if min_len == float("inf") else s[start:start+min_len]


        
