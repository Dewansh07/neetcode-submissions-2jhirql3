class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 =len(word1)
        w2 = len(word2)
        mi = min(w1,w2)
        res = []
        for i in range(mi):
            res.append(word1[i])
            res.append(word2[i])
        if w1>w2:
            res.extend(word1[w2:])
        elif w2>w1:
            res.extend(word2[w1:])
        return ''.join(res)
