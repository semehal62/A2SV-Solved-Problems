class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = Counter(nums)
        s_dict = sorted(dict1.items(), key = lambda x:(-x[1],x[0]))
        return [s_dict[i][0] for i in range(k)]
