class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        coll = []
        l,r = 0,0
        coll.append([nums1[0]+ nums2[0],0,0])
        stack = []
        seen = set()
        while len(coll) < k and (l < len(nums1) or r < len(nums2)):
            s,l,r = coll[-1]
            if r + 1 == len(nums2):
                op1 = (nums1[l+1]+ nums2[r],l+1,r)
                if op1 not in seen:
                    heappush(stack,op1)
                    seen.add(op1)
            elif l + 1 == len(nums1):
                op2 = (nums1[l] + nums2[r+1],l,r+1)
                if op2 not in seen:
                    heappush(stack,op2)
                    seen.add(op2)
            else:
                op1 = (nums1[l+1]+ nums2[r],l+1,r)
                op2 = (nums1[l] + nums2[r+1],l,r+1)
                if op1 not in seen:
                    heappush(stack,op1)
                    seen.add(op1)
                if op2 not in seen:
                    heappush(stack,op2)
                    seen.add(op2)

            coll.append(heappop(stack))
                
                
        ans = []

        for s,a,b in coll:
            ans.append([nums1[a],nums2[b]])

        return ans
