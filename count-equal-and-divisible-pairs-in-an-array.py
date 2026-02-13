class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        number = defaultdict(list)

        for i in range(len(nums)):
            number[nums[i]].append(i)

        count = 0
        for val in number.values():
            if len(val) > 1:
                print(val)
                for j in range(len(val)):
                    for w in range(j,len(val)):
                        if (val[j] * val[w]) % k == 0  and j != w:
                            count += 1
                               

        return count 
