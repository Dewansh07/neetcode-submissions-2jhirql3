class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic.get(key).append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        key_values = self.dic[key]

        l = 0
        r = len(key_values)-1
        res = ''
        while l<=r:
            mid = (l+r)//2
            key_time = key_values[mid][0]
            key_val = key_values[mid][1]

            if key_time == timestamp:
                return key_val
            elif key_time<timestamp:
                l = mid+1
                res = key_val
            else:
                r = mid-1
        return res
        
