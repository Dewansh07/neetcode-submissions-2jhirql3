class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.dic[key]:
            return ''
        key_values = self.dic[key]

        left,right = 0,len(key_values)-1
        result = ''
        while left<= right:
            mid = left + (right- left)//2

            key_time = key_values[mid][0]
            key_value = key_values[mid][1]
            if key_time == timestamp:
                return key_value
            elif key_time <= timestamp:
                result = key_value
                left = mid+1
            else:
                right = mid-1
        return result

