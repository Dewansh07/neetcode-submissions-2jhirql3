class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task = [(e,p,i) for i, (e,p) in enumerate(tasks)]
        task.sort()

        heap = []
        time = 0
        i = 0
        ans = []
        n = len(task)

        while i <n or heap:
            if not heap and time< task[i][0]:
                time = task[i][0]

            while i <n and task[i][0]<= time:
                e,p,idx = task[i]
                heapq.heappush(heap, (p,idx))
                i+=1

            process,idx = heapq.heappop(heap)
            time+=process
            ans.append(idx)
        return ans