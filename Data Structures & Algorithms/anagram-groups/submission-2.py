class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            sort = tuple(sorted(i))

            if sort in dic:
                dic[sort].append(i)
            else:
                dic[sort] = [i]
        return list(dic.values())