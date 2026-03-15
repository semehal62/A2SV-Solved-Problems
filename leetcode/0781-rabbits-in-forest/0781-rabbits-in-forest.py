class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)

        ans = 0
        minus = 0
        for key ,val in count.items():
            ans += (ceil(val / (key + 1)) * (key +1))

        return ans 

        