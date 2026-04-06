class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        if nums2 and nums1:
            arr = nums1 + nums2
        elif nums2:
            arr = nums2
        else:
            arr = nums1

        arr.sort()
    
        if len(arr) & 1:
            idx1 = (len(arr) + 1)//2
            idx1 -= 1
            return arr[idx1]   
        else:
            idx1 = len(arr)//2
            idx2 = idx1
            idx1 -= 1
            return ((arr[idx1] + arr[idx2])/2) 
            
                