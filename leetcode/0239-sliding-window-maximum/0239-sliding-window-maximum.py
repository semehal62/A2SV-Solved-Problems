class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        container = deque()

        for i in range(k):
            while container and container[-1] < nums[i]:
                container.pop()
            container.append(nums[i])
        
        arr = [container[0]]

        left = 0
        for right in range(k,len(nums)):
            if nums[left] == container[0]:
                container.popleft()
            while container and container[-1] < nums[right]:
                container.pop()
            container.append(nums[right])

            
            arr.append(container[0])
            left += 1


        return arr
