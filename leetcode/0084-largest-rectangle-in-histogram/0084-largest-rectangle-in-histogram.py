class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        queue = deque()
        right_bounds = [len(heights)]* len(heights)
        left_bound = [-1] * len(heights)


        for right in range(len(heights)):
   
            while queue and heights[queue[-1]] > heights[right]:
                right_bounds[queue[-1]]  = right 
                queue.pop()
            queue.append(right)

        queue = deque()
        for right in range(len(heights)-1,-1,-1):
   
            while queue and heights[queue[-1]] > heights[right]:
                left_bound[queue[-1]]  = right 
                queue.pop()
            queue.append(right)

        
        area = 0
        for i in range(len(heights)):
            area = max(area,(right_bounds[i]-left_bound[i]-1) * heights[i])

            
        return area