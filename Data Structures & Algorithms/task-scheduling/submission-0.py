class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        h = [-i for i in freq.values()]
        heapq.heapify(h)

        time = 0
        cooldown = deque()

        while h or cooldown:
            time+=1
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(h, cooldown.popleft()[1])

            if h:
                cnt = heapq.heappop(h)
                cnt+=1

                if cnt!=0:
                    cooldown.append((time+n+1, cnt))
        return time