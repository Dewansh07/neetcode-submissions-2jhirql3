class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed), reverse=True)
        stack = []
        # fleet = curtime = 0

        for dis, speed in pairs:
            des_time = (target - dis)/speed
            stack.append(des_time)

            if len(stack)>1 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)

        #     if curtime< des_time:
        #         fleet+=1
        #         curtime = des_time
        # return fleet
