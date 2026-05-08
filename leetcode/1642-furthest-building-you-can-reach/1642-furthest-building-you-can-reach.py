class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []

        for i in range(len(heights)):
            if i == len(heights)-1:
                arr.append(0)
            else:
                val = heights[i+1] - heights[i]
                if val < 0:
                    arr.append(0)
                else:
                    arr.append(val)

        cost = []
        ans = 0
        for i in range(len(arr)):
            if arr[i] <= bricks:
                heappush(cost,-arr[i])
                bricks -= arr[i]
            elif arr[i] > bricks:
                if  ladders > 0:
                    heappush(cost,-arr[i])
                    rm = -heappop(cost)
                    bricks += (rm - arr[i])
                    ladders -= 1
                else:
                    ans = i
                    break
            ans = i
        

        return ans




