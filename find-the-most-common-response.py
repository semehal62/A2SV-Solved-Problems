class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        arr = []
        for respons in responses:
            c_respons = Counter(respons)
            arr.extend(c_respons.keys())
           

        arr = list(arr)
        total = Counter(arr)
        
        maxi = max(total.values())
        mini = max(total)
        for key ,val in total.items():
            if val == maxi:
                mini = min(mini,key)

        return mini
