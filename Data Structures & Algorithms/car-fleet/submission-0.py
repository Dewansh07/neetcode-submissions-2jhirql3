class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleet = curtime = 0

        for dis, speed in sorted(pairs, reverse = True):
            des_time = (target - dis)/speed

            if curtime< des_time:
                fleet+=1
                curtime = des_time
        return fleet