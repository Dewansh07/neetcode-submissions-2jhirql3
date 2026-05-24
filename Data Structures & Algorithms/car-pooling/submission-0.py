class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_location =0
        for trip in trips:
            max_location = max(max_location, trip[2])

        pass_at_loc = [0]*(max_location+1)

        for trip in trips:
            n, frm , to = trip
            pass_at_loc[frm]+=n
            pass_at_loc[to]-=n

        current = 0
        for pasg in pass_at_loc:
            current+=pasg
            if current > capacity:
                return False
        return True