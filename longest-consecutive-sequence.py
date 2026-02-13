class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count_num = Counter(nums)
        ranges = defaultdict(int)
        maximum = 1
        if len(nums) == 0:
            return 0

        seen  = set()
        for key ,val in count_num.items():
            if key + 1 in ranges:
                ranges[key] = ranges[key + 1] + 1
                maximum = max(maximum,ranges[key + 1] + 1)
            else:
                if key + 1 in count_num:
                    temp = key + 1
                    count = 1
                    while temp  in count_num:
                        if temp in seen:
                            break
                        if temp in ranges:
                            ranges[key] = ranges[temp]  + count
                            maximum = max(maximum,ranges[temp] + count)
                            break
                        seen.add(temp)
                        temp += 1
                        count += 1
                    else:
                        ranges[key] = count
                        maximum = max(maximum,count)
                else:
                    ranges[key] = 1
                    
                

        return maximum  if maximum - 1 > 0 else 1
