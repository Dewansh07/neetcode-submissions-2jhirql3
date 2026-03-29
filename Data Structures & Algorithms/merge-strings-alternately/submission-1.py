class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        l1 = len(word1)
        l2 = len(word2)

        for i in range(min(l1,l2)):
            res.append(word1[i])
            res.append(word2[i])
        if l1<l2:
            res.append(word2[l1:])
        elif l2<l1:
            res.append(word1[l2:])
        return ''.join(res)