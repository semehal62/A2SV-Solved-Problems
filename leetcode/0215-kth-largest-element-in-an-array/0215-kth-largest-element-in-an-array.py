class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k 

        def quicksort(nums,k):
            pivot = random.choice(nums)

            left = [x for x in nums if x < pivot]
            mid = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]

            L = len(left)
            M = len(mid) 
            if k < L:
                return quicksort(left,k)
            elif k < L + M:
                return mid[0]
            else:
                return quicksort(right, k - L - M)
        

            
           

        return quicksort(nums,k)


