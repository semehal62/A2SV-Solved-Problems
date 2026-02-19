class Solution:
    def swap(self, arr, k):
        l = 0
        r = k
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
        return arr
    def pancakeSort(self, arr: List[int]) -> List[int]:

        right = len(arr)-1 
        
        ans = []
        n = 4
        while right != 0 :
            maxi  = max(arr[0:right+1])
            index  = arr.index(maxi)
            if index != right and  index != 0:
                ans.append(index+1)
                arr = self.swap(arr,index)
            else:
                if index == 0 and right != 0:
                   arr = self.swap(arr,right)
                   ans.append(right+1)
                right -= 1


        return ans
