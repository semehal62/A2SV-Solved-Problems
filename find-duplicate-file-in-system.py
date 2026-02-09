class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for path in paths:
            arr = path.split(" ")
            for i in range(1,len(arr)):
                number, filed = arr[i].split(".")
                dict1[filed].append(arr[0]+"/"+number+".txt")
        ans = []
        for key,value in dict1.items():
            if len(value) >1:
                ans.append(value)

        return ans
