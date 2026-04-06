class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def checker(radius):
            seen = set()
            for i in range(len(houses)):
                low = bisect_right(heaters,houses[i] - radius )
                highest = bisect_right(heaters,houses[i] - radius )
                if highest - low == 0:
                    return False
                else:
                    continue

            return True

        arr = []
        for i in range(len(houses)):
            idx = bisect_right(heaters,houses[i])
          

            if idx < len(heaters):
                dist_right = heaters[idx]- houses[i]
            else:
                dist_right = float("inf")

            if idx > 0:
                dist_left = houses[i] - heaters[idx-1] 
            else:
                dist_left = float("inf")
            

            

            arr.append(min(dist_left,dist_right))

      
        left = min(arr)
        right = max(arr)
    
        if left == right:
            return right

        while left <= right:
            mid = (left + right) //2

            if checker(mid):
                right = mid - 1   
            else:
                left = mid + 1



        
        return right

        
        