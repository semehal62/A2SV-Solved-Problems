class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        stack = []
        stack.append(points[0])
        for i in  range(1,len(points)):
            a,b = stack.pop()
            c,d = points[i]
            if b >= c:
                stack.append([c,min(b,d)])
            else:
                stack.append([a,b])
                stack.append([c,d])

        
        return len(stack)
