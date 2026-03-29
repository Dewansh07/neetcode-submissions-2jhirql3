class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            seen = set()
            temp = 0
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    temp+=1
                else:
                    break
            count = max(count,temp)
        return count
            
