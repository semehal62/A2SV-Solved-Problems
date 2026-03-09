class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        val = defaultdict(lambda:-1)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
            val[nums2[i]]

        ans = []
        for i in range(len(nums1)):
            ans.append(val[nums1[i]])

        return ans 

        