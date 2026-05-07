class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        tasks = [[tasks[i][0],tasks[i][1],i] for i in range(len(tasks))]
    
        heapify(tasks)
        time = 0
        small = heappop(tasks)
        time += small[0] + small[1]
        ans.append(small[2])
        store = []

        while tasks or store:
            while tasks and  tasks[0][0] <= time:
                val =  heappop(tasks)
                heappush(store,val[1:])

            if not store:
                x = heappop(tasks)
                ans.append(x[2])
                time = x[0] 
                time += x[1]
            else:
                x = heappop(store)
                ans.append(x[1])
                time += x[0]

        return ans

        