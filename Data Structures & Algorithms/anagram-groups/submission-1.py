class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            char = tuple(sorted(i))

            if char in dic:
                dic[char].append(i)
            else:
                dic[char] = [i]
        return list(dic.values())