class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0
        
    def push(self, val: int) -> None:
        # add the elemt:freq in the freq dict
        f = self.freq.get(val,0)+1
        self.freq[val] = f

        # now update the grouping {freq:[elemets with freq in list]}
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

        # update the self.maxfreq with maxfreq
        self.maxfreq = max(self.maxfreq,f)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()

        self.freq[val]-=1

        if not self.group[self.maxfreq]:
            self.maxfreq-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()